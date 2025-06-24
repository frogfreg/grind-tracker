class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getDistance(self):
        return ((self.x**2) + (self.y**2)) ** (1 / 2)

    def __lt__(self, other):
        return self.getDistance() < other.getDistance()


def kClosest(points, k):
    pointList = [Point(p[0], p[1]) for p in points]
    sortedPoints = sorted(pointList)

    finalPoints = [[p.x, p.y] for p in sortedPoints[:k]]

    return finalPoints
