import math
import stdarray
import stdstats


class AltRawDataStatistics:

    def __init__(self):
        self._points = []
    
    def addPoint(self, point):
        self._points += [point]

    def getNumPoints(self):
        return len(self._points)

    def getMean(self):
        return sum(self._points) / len(self._points)

    def getStdDev(self):
        return math.sqrt(self.getVariance())

    def getVariance(self):
        sumOfSquares = sum([x**2 for x in self._points])
        return sumOfSquares/len(self._points) - self.getMean()**2


class RawDataStatistics:

    def __init__(self, maxNumberOfPoints):
        self._maxNumberOfPoints = maxNumberOfPoints
        self._points = stdarray.create1D(self._maxNumberOfPoints)
        self._numPoints = 0
    
    def addPoint(self, point):
        self._points[self._numPoints] = point
        self._numPoints += 1

    def getNumPoints(self):
        return self._numPoints

    def getMean(self):
        points = self._points[:self._numPoints]
        return sum(points) / len(points)

    def getStdDev(self):
        return math.sqrt(self.getVariance())

    def getVariance(self):
        points = self._points[:self._numPoints]
        sumOfSquares = sum([x**2 for x in points])
        return sumOfSquares/len(points) - self.getMean()**2


class SumStoringStatistics:

    def __init__(self):
        self._sumOfValues = 0
        self._sumOfSquaredValues = 0
        self._numPoints = 0

    def addPoint(self, point):
        self._sumOfValues += point
        self._sumOfSquaredValues += point**2
        self._numPoints += 1

    def getNumPoints(self):
        return self._numPoints
    
    def getMean(self):
        return self._sumOfValues / self._numPoints

    def getStdDev(self):
        return math.sqrt(self.getVariance())

    def getVariance(self):
        return self._sumOfSquaredValues / self._numPoints - self.getMean()**2


def main():
    classes = [AltRawDataStatistics, RawDataStatistics, SumStoringStatistics]
    for c in classes:
        print(c.__name__)
        try:    obj = c(10)
        except: obj = c()
        obj.addPoint(0.1)
        obj.addPoint(0.3)
        obj.addPoint(0.5)
        print(f"N  = {obj.getNumPoints()}")
        print(f"μ  = {obj.getMean()}")
        print(f"σ² = {obj.getVariance()}")
        print(f"σ  = {obj.getStdDev()}")

    import numpy as np
    vals = [0.1, 0.3, 0.5]
    print("Oracle truth:")
    print(f"N  = {len(vals)}")
    print(f"μ  = {np.mean(vals)}")
    print(f"σ² = {np.var(vals)}")
    print(f"σ  = {np.std(vals)}")


if __name__ == "__main__":
    main()
