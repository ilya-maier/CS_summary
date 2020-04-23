def custom_map(array, fun):
    arr = []
    for i in array:
        arr.append(fun(i))
    return arr


arr = [1, 2, 3, 4, 5]
arr = custom_map(arr, lambda x: x * 10)
print(arr)
