from jinja2 import Environment, FileSystemLoader
from collectInput import *
from utils import *
import os

OUTPUT_DIR = "./output"

# Remove all files in output dir
for file in os.scandir(OUTPUT_DIR):
    os.remove(file.path)


environment = Environment(loader=FileSystemLoader("templates/"))
# userInputObj = getUserInput()
userInputObj = getTestData()

templateNames = ["type.txt", "mutation.txt", "mutation.medium-test.txt"]

for templateName in templateNames:
    template = environment.get_template(templateName)
    fileName = f"{userInputObj.getFileNamePrefix()}.{swapExtension(templateName, 'ts')}"

    content = template.render({"data": userInputObj})

    with open(os.path.join(OUTPUT_DIR, fileName), mode="w", encoding="utf-8") as file:
        file.write(content)
        print(f"... wrote {fileName}")

# # Generate _.type.ts
# typeFileTemplate = environment.get_template("type.txt")
# typeFileName = f"{userInputObj.getFileNamePrefix()}.type.ts"

# content = typeFileTemplate.render({"data": userInputObj})

# with open(os.path.join(OUTPUT_DIR, typeFileName), mode="w", encoding="utf-8") as file:
#     file.write(content)
#     print(f"... wrote {typeFileName}")


# # Generate _.mutation.ts
# mutationFileTemplate = environment.get_template("mutation.txt")
# mutationFileName = f'{fileNamePrefix}.mutation.ts'

# content = mutationFileTemplate.render({
#     'endpoint_name': endpointName,
#     'endpoint_full_name': endpointFullName,
#     'type_file_name_for_import': getFileNameWithoutExtension(typeFileName),
#   }
# )

# with open(os.path.join(OUTPUT_DIR, mutationFileName), mode="w", encoding="utf-8") as file:
#     file.write(content)
#     print(f"... wrote {mutationFileName}")


# # Generate _.mutation.medium-test.ts
# mutationMediumTestFileTemplate = environment.get_template("mutation.medium-test.txt")
# mutationMediumTestFileName = f'{fileNamePrefix}.mutation.medium-test.ts'

# content = mutationMediumTestFileTemplate.render({
#     'endpoint_name': endpointName
#   }
# )

# with open(os.path.join(OUTPUT_DIR, mutationMediumTestFileName), mode="w", encoding="utf-8") as file:
#     file.write(content)
#     print(f"... wrote {mutationMediumTestFileName}")


# TODO: Fix module not found error in userInput.py with importing field type
# Add the ability to have no input / output fields
