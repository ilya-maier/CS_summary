# helpers file that should reduce boilerplate code
import time
from random import random


def test_sorting_algorithm(sort=None, n=1000, returns=False):
    print(f"{sort.__name__}:")

    arr = [int(random() * n) for _ in range(n)]
    print(arr)

    start = time.time()
    if returns:
        arr = sort(arr)
    else:
        sort(arr)
    end = time.time()

    print(arr)
    print(f"Time elapsed: {end - start}\n")
