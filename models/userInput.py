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
