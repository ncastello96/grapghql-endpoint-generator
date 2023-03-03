from utils import *
from models.fieldTypeEnum import fieldTypes, booleanOptions, enterFieldsMenuOptions
from models.field import Field
from models.userInput import UserInput


def getUserInput():
    endpointType = getAndValidateEndpointType()
    endpointName = getAndValidateEndpointName(endpointType)
    inputFields = getInputFields()
    outputFields = getOutputFields()
    return UserInput(endpointType, endpointName, inputFields, outputFields)


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

    while not isPascalCase(response):
        response = input(f"Enter the name of the GQL {endpointType} (PascalCase): ")

    return response


def getInputFields():
    fields = []
    choice = None
    print("Input Fields: ")
    while choice != enterFieldsMenuOptions.index("Done"):
        fields.append(getAndValidateField())
        choice = int(
            input(menuToString("Select an option below", enterFieldsMenuOptions))
        )
    return fields


def getOutputFields():
    fields = []
    choice = None
    print("Output Fields: ")
    while choice != enterFieldsMenuOptions.index("Done"):
        fields.append(getAndValidateField())
        choice = int(
            input(menuToString("Select an option below", enterFieldsMenuOptions))
        )
    return fields


def getAndValidateField():
    name = ""
    while not isCamelCase(name):
        name = input("Enter the variable name (camelCase): ")

    choice = None
    while not isValidChoice(choice, getNumericalChoicesForMenuItems(fieldTypes)):
        choice = int(
            input(menuToString("Enter which type represents the field", fieldTypes))
        )
    fieldType = fieldTypes[choice]

    choice = None
    while not isValidChoice(choice, getNumericalChoicesForMenuItems(booleanOptions)):
        choice = int(input(menuToString("Is this field required?", booleanOptions)))
    required = booleanOptions[choice]

    description = input("Enter a description for this field: ")

    return Field(name, fieldType, required, description)


def getTestData():
    endpointType = "Mutation"
    endpointName = "AuditLogChanges"
    inputFields = [
        Field("transactionId", "Integer", True, "The id of the transaction"),
        Field("model", "String", True, "The model of the change"),
        Field("fromValue", "String", True, "The before value"),
        Field("toValue", "String", True, "The after value"),
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
