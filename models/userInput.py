from utils import lowerCaseFirstLetter, convertPascalToKebab

# from field import Field


class UserInput:
    def __init__(
        self,
        endpointType: str,
        endpointName: str,
        inputFields,
        outputFields,
    ) -> None:
        self.endpointType = endpointType
        self.endpointName = endpointName
        self.inputFields = inputFields
        self.outputFields = outputFields

    def getEndpointFullName(self):
        return f"{lowerCaseFirstLetter(self.endpointName)}{self.endpointType}"

    def getFileNamePrefix(self):
        return convertPascalToKebab(self.endpointName)

    def getTypeFileForImport(self):
        return f"{self.getFileNamePrefix()}.type"

    # To resolve imports in templates
    def hasInputFields(self):
        if self.inputFields:
            return True
        return False

    def hasOutputFields(self):
        if self.outputFields:
            return True
        return False

    def hasRequiredFields(self):
        allFields = self.inputFields + self.outputFields
        for field in allFields:
            if field.required:
                return True
        return False

    # TODO: Need to deal with enums, list and other types
    def getAllUniqueGqlTypes(self):
        allFields = self.inputFields + self.outputFields
        allGqlTypes = [x.gqlType for x in allFields]
        return list(set(allGqlTypes))


# class UserInput:
#     def __init__(
#         self,
#         endpointType: str,
#         endpointName: str,
#         inputFields: list[Field],
#         outputFields: list[Field],
#     ) -> None:
#         self.endpointType = endpointType
#         self.endpointName = endpointName
#         self.inputFields = inputFields
#         self.outputFields = outputFields

#     def getEndpointFullName(self):
#         return f"{lowerCaseFirstLetter(self.endpointName)}{self.endpointType}"

#     def getFileNamePrefix(self):
#         return convertPascalToKebab(self.endpointName)
