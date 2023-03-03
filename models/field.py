from menus.typeMenu import convertInputToGqlType, convertInputToTsType


class Field:
    def __init__(
        self, name: str, fieldType: str, required: bool, description: str
    ) -> None:
        self.name = name
        self.gqlType = convertInputToGqlType(fieldType)
        self.tsType = convertInputToTsType(fieldType)
        self.required = required
        self.description = description

    def __repr__(self) -> str:
        return f"{self.name}\n{self.gqlType}\n{self.tsType}\n{self.required}\n{self.description}"
