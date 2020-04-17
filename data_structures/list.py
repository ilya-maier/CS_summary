class List:

    def __init__(self, *elements):
        self.array = []
        self.array += elements
        self.length = len(elements)

    def __repr__(self):
        return self.array.__repr__()

    def push(self, value):
        self.array = self.array + [value]
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise RuntimeError("There are no elements in the list!")

        value = self.array[self.length - 1]
        self.array = self.array[:self.length - 1]
        self.length -= 1
        return value

    def add(self, value, index):
        self.check_index(index)
        self.push(None)

        for i in range(self.length - 1, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value

    def get(self, index):
        self.check_index(index)
        return self.array[index]

    def remove(self, index):
        self.check_index(index)

        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.array = self.array[:self.length - 1]
        self.length -= 1

    def index_of(self, value):
        for i in range(self.length - 1):
            if self.array[i] == value:
                return i
        return -1

    def check_index(self, index):
        if index < 0 or index >= self.length:
            raise ValueError("Given index is incorrect!")


arr = List(5, 4, 3, 2, 1)
print(arr)

arr.pop()
arr.push(0)
arr.add(value=-1, index=2)
arr.remove(3)
index = arr.index_of(2)  # -> 3
element = arr.get(0)  # -> 5
# it now should be [5, 4, -1, 2, 0]
print(arr)
print(f"Index: {index}")
print(f"Length: {arr.length}")
print(f"Element: {element}")
