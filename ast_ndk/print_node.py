class PrintNode:

    def __init__(self, value) -> None:
        self.value = value 
    
    def __repr__(self) -> str:
           return f"PrintNode({self.value})"
