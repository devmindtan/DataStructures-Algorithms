import heapq


def getThreeLargest(arr):
    return heapq.nlargest(3, list(set(arr)))


arr = [10, 4, 3, 50, 23, 90, 90]
print(getThreeLargest(arr))
