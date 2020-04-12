"""
    Bubble Sort:
        swaps two numbers in the whole array and repeats doing it until sorted
    Time Complexity: O(n^2) -> worst
    Space Complexity: O(1)

    https://en.wikipedia.org/wiki/Bubble_sort
"""
from random import random


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swapped = True


arr = [int(random() * 100) for _ in range(100)]
print(arr)
bubble_sort(arr)
print(arr)
