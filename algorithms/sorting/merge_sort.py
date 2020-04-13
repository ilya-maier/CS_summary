"""
    Merge Sort:
        divides the list to single elements and then compare each element
        to teh adjacent array and merge them until done
    Time Complexity: O(n*log(n)) -> worst
    Space Complexity: O(n)

    https://en.wikipedia.org/wiki/Merge_sort
"""
from helpers import test_sorting_algorithm


def merge(arr1, arr2):
    array = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            array.append(arr1[i])
            i += 1
        else:
            array.append(arr2[j])
            j += 1
    if i == len(arr1):
        array.extend(arr2[j:])
    else:
        array.extend(arr1[i:])
    return array


def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    return merge(merge_sort(arr[:int(length / 2)]),
                 merge_sort(arr[int(length / 2):]))


test_sorting_algorithm(merge_sort, returns=True)
