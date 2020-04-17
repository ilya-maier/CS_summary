"""
    Quick Sort:
        chooses a pivot (last element) and splits the array into
        smaller and larger part and then does quick_sort() on both of the parts
        and concatenates smaller part, pivot and the bigger part
    Time Complexity: O(n*log(n)) -> average
                     O(n^2) -> worst
    Space Complexity: O(log(n))

    https://en.wikipedia.org/wiki/Quicksort
    https://stackoverflow.com/questions/18262306/quicksort-with-python
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


def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    # each element between arr[begin] and arr[pivot] is <= than arr[begin],
    # therefore we need to swap them
    arr[pivot], arr[begin] = arr[begin], arr[pivot]

    return pivot


def quicksort_in_place(arr, begin=0, end=None):
    if end is None:
        end = len(arr)

    if begin >= end:
        return

    pivot = partition(arr, begin, end)
    quicksort_in_place(arr, begin, pivot)
    quicksort_in_place(arr, pivot + 1, end)


test_sorting_algorithm(quicksort, returns=True)
test_sorting_algorithm(quicksort_in_place)
