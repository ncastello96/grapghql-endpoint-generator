class Field:
    def __init__(
        self, name: str, fieldType: str, required: bool, description: str
    ) -> None:
        self.name = name
        self.gqlType = "temp"
        self.tsType = "temp"
        self.required = required
        self.description = description

    def __repr__(self) -> str:
        return f"{self.name}\n{self.gqlType}\n{self.tsType}\n{self.required}\n{self.description}"
