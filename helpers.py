# helpers file that should reduce boilerplate code
import time
from random import random


def test_sorting_algorithm(sort=None, version="normal", returns=False, n=1000):
    if version.lower() == "normal":
        print("Normal version:")
    else:
        print("Optimized version:")
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
