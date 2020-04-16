"""
    Insertion Sort:
        inserts each element into already sorted array until done
    Time Complexity: O(n^2) -> worst
    Space Complexity: O(1)

    https://en.wikipedia.org/wiki/Insertion_sort
"""
from helpers import test_sorting_algorithm


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1


test_sorting_algorithm(insertion_sort)
