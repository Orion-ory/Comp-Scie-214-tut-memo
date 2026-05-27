# Author:           Rijk de Wet
# Last modified:    30 Jan 2023

import stdstats
import stdarray
import stdrandom

from typing import List


def accumulate(array:List[float]) -> List[float]:
    """
    Take a probability density function as a list
    of `float`s and return its cumulative density
    function.
    #### Examples
    ```
    accumulate([1, 1, 1]) == [1, 2, 3]
    accumulate([1, 2, 3]) == [1, 3, 6]
    accumulate([3, 2, 1]) == [3, 5, 6]
    ```
    """
    accumulated:List[float] = stdarray.create1D(len(array), 0.0)
    currentSum:float = 0
    for i in range(len(array)):
        currentSum += array[i]
        accumulated[i] = currentSum
    return accumulated


def discrete(a:List[float], k:int) -> float:
    """
    Generate `k` integers in range `[0, len(a)-1]`
    where each index `i` of list `a` is
    associated with the probability `a[i]`.
    `sum(a)` must be `== 1`.  Uses a binary
    search algorithm for speed.
    """
    # Ensure that the probabilities do add up to 1
    assert sum(a) == 1
    # Obtain `s`, which is the CDF to the PDF that is `a`.
    s:List[float] = accumulate(a)
    # Start sampling
    values = []
    for i in range(k):
        # the probability between 0 and 1
        probability:float = stdrandom.uniformFloat(0, 1)
        # indices to binary search with
        lo:int = 0
        hi:int = len(s)-1
        # binary search starts here.  non-recursive version.
        while lo+1 < hi:
            mid:int = (lo+hi)//2  # integer division, i.e. round result down
            if s[mid] <= probability:
                lo = mid
            else:
                hi = mid
        if s[lo] > probability:
            values.append(lo)
        else:
            values.append(hi)
    return values
