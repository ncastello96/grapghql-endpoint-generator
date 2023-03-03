fieldTypes = ["Integer", "Float", "Boolean", "String", "Enum", "Other"]

booleanOptions = [True, False]

enterFieldsMenuOptions = ["Enter another field", "Done"]

inputToGqlTypeMap = {
    "Integer": "GraphQLInt",
    "Float": "GraphQLFloat",
    "Boolean": "GraphQLBoolean",
    "String": "GraphQLString",
}

gqlToTsTypeMap = {
    "Integer": "number",
    "Float": "number",
    "Boolean": "boolean",
    "String": "string",
}
