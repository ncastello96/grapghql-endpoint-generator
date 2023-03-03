from utils import upperCaseFirstLetter, convertCamelToKebab, lowerCaseFirstLetter

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
        return f"{self.endpointName}{self.endpointType}"

    def getFileNamePrefix(self):
        return convertCamelToKebab(self.endpointName)

    def getTypeFileForImport(self):
        return f"{self.getFileNamePrefix()}.type"

    def getActionName(self):
        return self.endpointName

    def getEndpointNamePascalCase(self):
        return upperCaseFirstLetter(self.endpointName)

    def getEndpointTypeCamelCase(self):
        return lowerCaseFirstLetter(self.endpointType)

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

    def getAllUniqueGqlTypes(self):
        allFields = self.inputFields + self.outputFields
        # Hack to only return GQL types that are one word aka dont return placeholders for the import
        allGqlTypes = [x.gqlType for x in allFields if len(x.gqlType.split(" ")) == 1]
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
