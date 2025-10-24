def isSorted(arr):
    if (arr == sorted(arr)):
        return True
    return False


arr = [10, 20, 30, 40, 50]
arr = [90, 80, 100, 70, 40, 30]
print(isSorted(arr))
