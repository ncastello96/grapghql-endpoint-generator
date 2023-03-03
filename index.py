from jinja2 import Environment, FileSystemLoader
from collectInput import *
from utils import *
import os
import sys

OUTPUT_DIR = "./output"
TEMPLATES_DIR = "./templates"

# Remove all files in output dir
for file in os.scandir(OUTPUT_DIR):
    os.remove(file.path)


environment = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, lstrip_blocks=True
)

userInputObj = None
if len(sys.argv) > 1 and sys.argv[1] == "test":
    userInputObj = getTestData()
else:
    userInputObj = getUserInput()

templateNames = os.listdir(TEMPLATES_DIR)

for templateName in templateNames:
    template = environment.get_template(templateName)
    fileName = f"{userInputObj.getFileNamePrefix()}.{swapExtension(templateName, 'ts')}"

    content = template.render({"data": userInputObj})

    with open(os.path.join(OUTPUT_DIR, fileName), mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"... wrote {fileName}")


# TODO: Fix module not found error in userInput.py with importing field type
# Add the ability to have no input / output fields
# Figure out the resolve options
# Allow lists to be a type
# Allow dates to be a type
# Allow composite types to be entered (type within a type within a type...)
# Allow user to enter the name (and path?) of their action
# Possibly add default values for fields
# Fix case where user enters empty string and we try to cast to int in getInputFields
# THIS WILL CREATE QUERIES IN A .mutation file. Fix this! Need a query template or to change the name dynamically
