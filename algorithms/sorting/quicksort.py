"""
    Quick Sort:
        chooses a pivot (last element) and splits the array into
        smaller and larger part and then does quick_sort() on both of the parts
        and concatenates smaller part, pivot and the bigger part
    Time Complexity: O(n*log(n)) -> average
                     O(n^2) -> worst
    Space Complexity: O(log(n))

    https://en.wikipedia.org/wiki/Quicksort
"""
from helpers import test_sorting_algorithm


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    smaller_part = []
    larger_part = []
    pivot = arr[len(arr) - 1]
    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            smaller_part.append(arr[i])
        else:
            larger_part.append(arr[i])
    return quicksort(smaller_part) + [pivot] + quicksort(larger_part)


test_sorting_algorithm(quicksort, returns=True)
