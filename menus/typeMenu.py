typeOptions = ["Integer", "Float", "Boolean", "String", "Enum", "Other"]

inputToGqlTypeMap = {
    "Integer": "GraphQLInt",
    "Float": "GraphQLFloat",
    "Boolean": "GraphQLBoolean",
    "String": "GraphQLString",
    "Enum": "// Generate enum file and use that type here",
    "Other": "// FILL IN custom type here",
}

inputToTsTypeMap = {
    "Integer": "number",
    "Float": "number",
    "Boolean": "boolean",
    "String": "string",
    "Enum": "// FILL IN enum type here",
    "Other": "// FILL IN custom type here",
}


def convertInputToGqlType(inputType):
    return inputToGqlTypeMap[inputType]


def convertInputToTsType(inputType):
    return inputToTsTypeMap[inputType]
