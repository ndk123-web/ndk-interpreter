class PrintNode:

    def __init__(self, value, blocks = 0, identifier = None) -> None:
        self.value = value
        self.blocks = blocks
        self.identifier = identifier

    def __repr__(self) -> str:
           return f"PrintNode({self.value}, blocks={self.blocks}, identifier={self.identifier})"
