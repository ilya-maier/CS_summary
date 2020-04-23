def custom_filter(array, fun):
    arr = []
    for i in array:
        if fun(i):
            arr.append(i)
    return arr


arr = [1, 2, 3, 4, 5]
arr = custom_filter(arr, lambda x: x % 2 == 0)
print(arr)
