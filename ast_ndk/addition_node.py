class AdditionNode:
    def __init__(self, left, right, identifier_name=None):
        self.left = left
        self.right = right
        self.identifier_name = identifier_name

    def __repr__(self):
        return f"AdditionNode(left={self.left}, right={self.right}, result={self.left + self.right})"