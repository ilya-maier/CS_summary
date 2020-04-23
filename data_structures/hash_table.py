class HashTable:

    def __init__(self, size=1024, **kwargs):
        self.arr = [None] * size
        self.keys = []
        self.values = []
        self.length = 0
        self.size = size
        self.add(**kwargs)

    def __repr__(self):
        out = "{"
        for k in range(len(self.keys)):
            out += f"{self.keys[k]}: {self.values[k]}, "
        return out[:-2] + "}"

    def __len__(self):
        return self.length

    def add(self, **kwargs):
        for key, value in kwargs.items():
            self.keys.append(key)
            self.values.append(value)
            self.arr[self.custom_hash(key)] = value
            self.length += 1

    def get(self, key):
        return self.arr[self.custom_hash(key)]

    def remove(self, key):
        del self.values[self.keys.index(key)]
        self.keys.remove(key)
        self.arr[self.custom_hash(key)] = None

    def custom_hash(self, key):
        num = 0
        for i in range(len(key)):
            num += i * ord(key[i])
        return num % self.size


hash_table = HashTable(key=2, qwe=10, arr=123, first=-1)

print(hash_table)
print(hash_table.keys)
print(hash_table.values)

hash_table.add(test="test")
hash_table.remove("qwe")
print(hash_table)
print(hash_table.get("test"))
print(len(hash_table))
