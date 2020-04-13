"""
    Insertion Sort:
        inserts each element into already sorted array until done
    Time Complexity: O(n^2) -> worst
    Space Complexity: O(1)

    https://en.wikipedia.org/wiki/Insertion_sort
"""
import time
from random import random
from bisect import bisect_left


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1


# Time Complexity: O(n*log(n)) -> worst
# Space Complexity: O(n)
def insertion_sort_optimized(arr):
    array = [arr[0]]
    for i in range(1, len(arr)):
        index = bisect_left(array, i)
        array.insert(index, i)
    return array


print("Normal version:")
arr = [int(random() * 100) for _ in range(100)]
print(arr)

start = time.time()
insertion_sort(arr)
end = time.time()

print(arr)
print(f"Time elapsed: {end - start}\n")

print("Optimized version:")
arr = [int(random() * 100) for _ in range(100)]
print(arr)

start = time.time()
arr = insertion_sort_optimized(arr)
end = time.time()

print(arr)
print(f"Time elapsed: {end - start}\n")
