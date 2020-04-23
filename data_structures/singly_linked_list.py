from data_structures.nodes.node import Node


class SinglyLinkedList:
    head = None
    tail = None
    length = 0

    def __init__(self, *args):
        for arg in args:
            self.push(arg)

    def __repr__(self):
        out = ""
        node = self.head
        while node:
            out += f"{node.value}, "
            node = node.next
        return out[:- 2]

    def push(self, value):
        self.length += 1
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def pop(self):
        old_tail = self.tail
        new_tail = self.head

        for _ in range(self.length - 2):
            new_tail = new_tail.next

        new_tail.next = None
        self.tail = new_tail
        self.length -= 1

        return old_tail

    def get(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def remove(self, index):
        node = self.get(index - 1)
        out = node.next

        node.next = out.next
        self.length -= 1

        return out.value

    def find(self, value):
        index = 0
        node = self.head

        while node.value != value:
            if node.next is None:
                return -1

            node = node.next
            index += 1

        return index


list = SinglyLinkedList(4, 7, 1, 0)
print(list)
print(list.get(1))
print(list.remove(3))
print(list.find(1))
print(list)
