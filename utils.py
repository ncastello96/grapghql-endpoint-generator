import re
import os


def convertPascalToKebab(pascalCaseName):
    if not isPascalCase(pascalCaseName):
        print(f"The input {pascalCaseName} is not valid PascalCase!")
    return re.sub(r"(?<!^)(?=[A-Z])", "-", pascalCaseName).lower()


def getFileNameWithoutExtension(fileName):
    return os.path.splitext(fileName)[0]


def swapExtension(fileName, newExtension):
    return f"{getFileNameWithoutExtension(fileName)}.{newExtension}"


def lowerCaseFirstLetter(input):
    return f"{input[0].lower()}{input[1:]}"


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
