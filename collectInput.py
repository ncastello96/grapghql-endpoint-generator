from utils import *

from menus.booleanMenu import booleanOptions
from menus.typeMenu import typeOptions
from menus.enterFieldsMenu import enterFieldsOptions
from models.field import Field
from models.userInput import UserInput


def getUserInput():
    endpointType = getAndValidateEndpointType()
    endpointName = getAndValidateEndpointName(endpointType)
    endpointDescription = getendpointDescription(endpointType)
    inputFields = getInputFields()
    outputFields = getOutputFields()
    return UserInput(
        endpointType, endpointName, endpointDescription, inputFields, outputFields
    )


def getAndValidateEndpointType():
    response = None
    while not isValidChoice(response, ["m", "q"]):
        response = input("Is this a mutation (m) or a query (q)? ")

    if response == "m":
        return "Mutation"
    else:
        return "Query"


def getAndValidateEndpointName(endpointType):
    response = ""

    while not isCamelCase(response):
        response = input(f"Enter the name of the GQL {endpointType} (camelCase): ")

    return response


def getendpointDescription(endpointType):
    return input(f"Enter the description of this {endpointType}: ")


def getInputFields():
    fields = []
    choice = None
    print("Input Fields: ")
    while choice != enterFieldsOptions.index("Done"):
        fields.append(getAndValidateField())
        choice = int(input(menuToString("Select an option below", enterFieldsOptions)))
    return fields


def getOutputFields():
    fields = []
    choice = None
    print("Output Fields: ")
    while choice != enterFieldsOptions.index("Done"):
        fields.append(getAndValidateField())
        choice = int(input(menuToString("Select an option below", enterFieldsOptions)))
    return fields


def getAndValidateField():
    name = ""
    while not isCamelCase(name):
        name = input("Enter the variable name (camelCase): ")

    choice = None
    while not isValidChoice(choice, getNumericalChoicesForMenuItems(typeOptions)):
        choice = int(
            input(menuToString("Enter which type represents the field", typeOptions))
        )
    fieldType = typeOptions[choice]

    choice = None
    while not isValidChoice(choice, getNumericalChoicesForMenuItems(booleanOptions)):
        choice = int(input(menuToString("Is this field required?", booleanOptions)))
    required = booleanOptions[choice]

    description = input("Enter a description for this field: ")

    return Field(name, fieldType, required, description)


def getTestData():
    endpointType = "Mutation"
    endpointName = "auditLogChanges"
    inputFields = [
        Field("transactionId", "Integer", True, "The id of the transaction"),
        Field("model", "String", True, "The model of the change"),
        Field("fromValue", "String", True, "The before value"),
        Field("toValue", "String", True, "The after value"),
        Field("type", "Enum", False, "The originator (external, system, or user)"),
    ]
    outputFields = [
        Field(
            "numChangesWritten",
            "Integer",
            True,
            "The number of changes written to the database",
        ),
        Field(
            "numTransactionsWritten",
            "Integer",
            True,
            "The number of transactions written to the database",
        ),
    ]
    return UserInput(endpointType, endpointName, inputFields, outputFields)
