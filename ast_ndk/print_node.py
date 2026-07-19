class PrintNode:

    def __init__(self, value, blocks = 0) -> None:
        self.value = value
        self.blocks = blocks

    def __repr__(self) -> str:
           return f"PrintNode({self.value}, blocks={self.blocks})"
