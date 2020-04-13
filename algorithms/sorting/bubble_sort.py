"""
    Bubble Sort:
        swaps two numbers in the whole array and repeats doing it until sorted
    Time Complexity: O(n^2) -> worst
    Space Complexity: O(1)

    https://en.wikipedia.org/wiki/Bubble_sort
    https://en.wikipedia.org/wiki/XOR_swap_algorithm
"""
from helpers import test_sorting_algorithm


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


def bubble_sort_optimized(arr):
    swapped = True

    # don't go over the first and last, already sorted, parts
    first_swapped = 0
    last_swapped = 0
    index = len(arr)

    while swapped:
        swapped = False
        for i in range(first_swapped, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp

                """ 
                # one could also use xor swap, which does not instantiate the
                # temp variable, but it would actually be slower
                arr[i] = arr[i] ^ arr[i + 1]
                arr[i + 1] = arr[i] ^ arr[i + 1]
                arr[i] = arr[i] ^ arr[i + 1]
                """

                # optimization
                if not swapped and i != 0:
                    first_swapped = i - 1
                last_swapped = i

                swapped = True
            elif i > index:
                break
        index = last_swapped


test_sorting_algorithm(bubble_sort)
test_sorting_algorithm(bubble_sort_optimized, version="optimized")
