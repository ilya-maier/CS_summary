class HashTable:

    def __init__(self, size=1024, **kwargs):
        self.arr = [None] * size
        self.keys = []
        self.values = []
        self.size = size
        self.add(**kwargs)

    def __repr__(self):
        out = "{"
        for k in range(len(self.keys)):
            out += f"{self.keys[k]}: {self.values[k]}, "
        return out[:-2] + "}"

    def add(self, **kwargs):
        for key, value in kwargs.items():
            self.keys.append(key)
            self.values.append(value)
            self.arr[self.custom_hash(key)] = value

    def custom_hash(self, key):
        num = 0
        for i in range(len(key)):
            num += i * ord(key[i])
        return num % self.size


hash_table = HashTable(key=2, qwe=10, arr=123, first=-1)
print(hash_table)
print(hash_table.keys)
print(hash_table.values)
