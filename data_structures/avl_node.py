class AVLNode:
    value = None
    left = None
    right = None
    height = 1

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"

    def add(self, value):
        if value < self.value:
            if not self.left:
                self.left = AVLNode(value)
            else:
                self.left.add(value)

            if not self.right:
                self.height = self.left.height + 1
            elif self.right.height < self.left.height:
                self.height = self.left.height + 1

        elif value > self.value:
            if not self.right:
                self.right = AVLNode(value)
            else:
                self.right.add(value)

            if not self.left:
                self.height = self.right.height + 1
            elif self.left.height < self.right.height:
                self.height = self.right.height + 1
