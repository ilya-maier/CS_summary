class TreeNode:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"
