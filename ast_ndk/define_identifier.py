class DefineIdentifierNode:
    def __init__(self, identifier_name, value):
        self.identifier_name = identifier_name
        self.value = value

    def __repr__(self):
        return f"DefineIdentifierNode(identifier_name={self.identifier_name}, value={self.value})"