# Note that this example crashes because the worst-case recursion depth for large cases becomes too deep.
# The average case could handle far larger arrays.
# Importantly: the ratio in execution time when doubling the input array size for large arrays:
# - is close to 2 for the average case, suggesting linear/linearithmic performance
# - is close to 4 for the worst case, suggesting quadratic performance

import sys
from time import time 

import stdarray
import stdrandom
import stdio

def quicksort(a):
    sort(a, 0, len(a)-1)

def sort(a, low, hi):

    if low < hi:
        j = partition(a, low, hi)
        sort(a, low, j-1)
        sort(a, j+1, hi)

def partition(a, low, hi):

    p = a[hi]
    i = low-1

    for j in range(low, hi):
        if a[j] < p:
            i += 1
            swap(a, i, j)

    swap(a, i+1, hi)
    return i+1

def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def main():

    # Test our function with a list of 100 integers, with each value randomly sampled between
    # 0 and 1000

    a = [stdrandom.uniformInt(0, 1000) for i in range(100)]
    stdio.writeln("Our random values:")
    stdio.writeln(a)

    quicksort(a)
    stdio.writeln("\nSorted:")
    stdio.writeln(a)

    # Now that we are sure it works, let's do a time test with increasing array lengths. First we
    # will look at the average case, when the list is randomly shuffled. Then at the worst case, 
    # when the list is already sorted.

    sizes = [50 * 2 ** i for i in range(8)]

    stdio.writeln("\nAverage case time tests:")
    for size in sizes:
        stdio.writeln(f"  {size} elements:")

        a = [stdrandom.uniformInt(0, 1000000) for i in range(size)]

        # List sorted random order
        stdrandom.shuffle(a)
        start = time()
        quicksort(a)
        stdio.writeln(f"\tRandom order: {time() - start:.3f} seconds")

    try:
        stdio.writeln("\nWorst case time tests:")
        for size in sizes:

            stdio.writeln(f"  {size} elements:")

            a = [stdrandom.uniformInt(0, 1000000) for i in range(size)]

            # List sorted from ascending order
            quicksort(a)
            start = time()
            quicksort(a)
            stdio.writeln(f"\tAscending order: {time() - start:.3f} seconds")

            # List sorted from descending order
            a.reverse()
            start = time()
            quicksort(a)
            stdio.writeln(f"\tDescending order: {time() - start:.3f} seconds")
    except RecursionError:
        stdio.writeln("Maximum recursive depth reached.")



if __name__ == "__main__":
    sys.setrecursionlimit(4000)

    main()
