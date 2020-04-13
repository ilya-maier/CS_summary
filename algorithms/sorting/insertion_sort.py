"""
    Insertion Sort:
        inserts each element into already sorted array until done
    Time Complexity: O(n^2) -> worst
    Space Complexity: O(1)

    https://en.wikipedia.org/wiki/Insertion_sort
"""
from bisect import bisect_left

from helpers import test_sorting_algorithm


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


test_sorting_algorithm(insertion_sort)
test_sorting_algorithm(insertion_sort_optimized,
                       version="optimized",
                       returns=True)
