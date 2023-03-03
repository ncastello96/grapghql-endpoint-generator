from jinja2 import Environment, FileSystemLoader
from collectInput import *
from utils import *
import os

OUTPUT_DIR = "./output"
TEMPLATES_DIR = "./templates"

# Remove all files in output dir
for file in os.scandir(OUTPUT_DIR):
    os.remove(file.path)


environment = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, lstrip_blocks=True
)
userInputObj = getUserInput()
# userInputObj = getTestData()

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
