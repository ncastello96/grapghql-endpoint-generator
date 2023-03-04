import re
import os


def convertCamelToKebab(camelCaseName):
    if not isCamelCase(camelCaseName):
        print(f"The input {camelCaseName} is not valid camelCase!")
    return re.sub(r"(?<!^)(?=[A-Z])", "-", camelCaseName).lower()


def getFileNameWithoutExtension(fileName):
    return os.path.splitext(fileName)[0]


def createFileNameFromTemplateName(userInput, templateName):
    # Input example: mutation_query.medium-test.txt
    ENDPOINT_TYPE_PLACEHOLDER = "mutation_query"

    # Replace the 'mutation_query' placeholder with the endpoint type (mutation OR query)
    # Ex mutation.medium-test.txt
    templateName = templateName.replace(
        ENDPOINT_TYPE_PLACEHOLDER, lowerCaseFirstLetter(userInput.endpointType)
    )
    # Add name
    # Ex audit-log-changes.mutation.medium-test.txt
    fileNameWithBadExtension = f"{userInput.getFileNamePrefix()}.{templateName}"
    # Put the correct extension
    # Ex audit-log-changes.mutation.medium-test.ts
    return swapExtension(fileNameWithBadExtension, "ts")


def swapExtension(fileName, newExtension):
    return f"{getFileNameWithoutExtension(fileName)}.{newExtension}"


def lowerCaseFirstLetter(input):
    return f"{input[0].lower()}{input[1:]}"


def upperCaseFirstLetter(input):
    return f"{input[0].upper()}{input[1:]}"


def isPascalCase(input):
    pascalCaseRegex = "^[A-Z][a-z]+(?:[A-Z][a-z]+)*$"
    if re.fullmatch(pascalCaseRegex, input):
        return True
    return False


def isCamelCase(input):
    camelCaseRegex = "^[a-z]+(?:[A-Z][a-z]+)*$"
    if re.fullmatch(camelCaseRegex, input):
        return True
    return False


def isValidChoice(choice, validOptions):
    return choice in validOptions


def getNumericalChoicesForMenuItems(menuItems):
    return [x for x in range(len(menuItems))]


def menuToString(prompt, validOptions):
    menu = [f"{prompt}:\n"]
    for idx, option in enumerate(validOptions):
        menu.append(f"{idx}) {option}\n")
    return "".join(menu)
