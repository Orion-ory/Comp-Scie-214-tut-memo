#-----------------------------------------------------------------------
# comparablecharge.py
# Modified version of charge.py to add comparable-ness
#-----------------------------------------------------------------------

import sys
import math
import stdio

#-----------------------------------------------------------------------

class Charge:

    # Construct self centered at (x, y) with charge q.
    def __init__(self, x0, y0, q0):
        self._rx = x0  # x value of the query point
        self._ry = y0  # y value of the query point
        self._q = q0   # Charge

    # Return the potential of self at (x, y).
    def potentialAt(self, x, y):
        COULOMB = 8.99e09
        dx = x - self._rx
        dy = y - self._ry
        r = math.sqrt(dx*dx + dy*dy)
        if r == 0.0: # Avoid division by 0
            if self._q >= 0.0:
                return float('inf')
            else:
                return float('-inf')
        return COULOMB * self._q / r

    # Return a string representation of self.
    def __str__(self):
        result = str(self._q) + ' at ('
        result += str(self._rx) + ', ' + str(self._ry) + ')'
        return result

    def __lt__(self, other): return self._q <  other._q
    def __le__(self, other): return self._q <= other._q
    def __eq__(self, other): return self._q == other._q
    def __ne__(self, other): return self._q != other._q
    def __gt__(self, other): return self._q >  other._q
    def __ge__(self, other): return self._q >= other._q

    

#-----------------------------------------------------------------------

# For testing.
# Creates a few charges and sorts them to test the comparable features

def main():
    charges = [
        Charge(0, 0, 3),
        Charge(0, 0, 5),
        Charge(0, 0, 4),
        Charge(0, 0, 2),
        Charge(0, 0, 1),
    ]
    charges_sorted = list(sorted(charges))
    for c in charges_sorted:
        stdio.writeln(c)
    

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

