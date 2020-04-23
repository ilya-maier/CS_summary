from data_structures.nodes.avl_node import AVLNode


def get_height(node):
    if node:
        return node.height
    else:
        return 0


class AVLTree:
    root = None
    length = 0

    def __init__(self, *args):
        for arg in args:
            self.add(arg)

    def __repr__(self):
        return self.root.__repr__()

    def __len__(self):
        return self.length

    def height(self):
        return self.root.height

    def add(self, value):
        if self.root is None:
            self.root = AVLNode(value)
        else:
            self.root.add(value)

        self.balance_tree()

    def balance_tree(self):
        node = self.root

        if self.height() > 3:
            if get_height(node.right.right) == get_height(node.right.left) + 2:
                self.rotate_right(node.right)
            elif get_height(node.right.right) + 2 == get_height(
                    node.right.left):
                self.rotate_left(node.right)

            elif get_height(node.left.right) == get_height(node.left.left) + 2:
                self.rotate_right(node.left)
            elif get_height(node.left.right) + 2 == get_height(node.left.left):
                self.rotate_left(node.left)

            elif get_height(node.right) == get_height(node.left) + 2:
                self.rotate_right(node)
            elif get_height(node.right) + 2 == get_height(node.left):
                self.rotate_right(node)

        elif get_height(node.right) == get_height(node.left) + 2:
            self.rotate_right(node)
        elif get_height(node.right) + 2 == get_height(node.left):
            self.rotate_right(node)

    def rotate_right(self, node):
        # swap root and its right child values
        node.value, node.right.value = \
            node.right.value, node.value

        # save root's left child for later
        left = node.left

        node.left = node.right
        node.right = node.right.right

        node.left.right = node.left.left
        node.left.left = left

        self.calc_height(node)
        self.balance_tree()

    def rotate_left(self, node):
        # swap root and its left child values
        node.value, node.left.value = \
            node.left.value, node.value

        # save root's right child for later
        right = node.right

        node.right = node.left
        node.left = node.left.left

        node.right.left = node.right.right
        node.right.right = right

        self.calc_height(node)
        self.balance_tree()

    def calc_height(self, node):
        node.right.height = max(
            get_height(node.right.right),
            get_height(node.right.left)) + 1
        node.left.height = max(
            get_height(node.left.right),
            get_height(node.left.left)) + 1
        node.height = max(
            get_height(node.right),
            get_height(node.left)) + 1

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


avl_tree = AVLTree(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(avl_tree)
