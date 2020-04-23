from data_structures.nodes.tree_node import TreeNode


class BinaryTree:
    root = None
    length = 0

    def __init__(self, *args):
        for arg in args:
            self.add(arg)

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        return self.length

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current = self.root
            inserted = False

            while not inserted:
                if value == current.value:
                    inserted = True

                if value < current.value:
                    if current.left is None:
                        current.left = TreeNode(value)
                        inserted = True
                    current = current.left

                else:
                    if current.right is None:
                        current.right = TreeNode(value)
                        inserted = True
                    current = current.right

        self.length += 1

    def get(self, value):
        current = self.root

        while current.value != value:
            if value > current.value:
                current = current.right
            else:
                current = current.left

            if not current:
                return -1

        return current.value


b_tree = BinaryTree(5, 3, 7, 5, 8, 12, 2)
print(b_tree)
print(len(b_tree))
print(b_tree.get(1))
