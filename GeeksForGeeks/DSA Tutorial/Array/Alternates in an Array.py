def getAlternates(arr):
    res = []
    for i in range(len(arr)):
        if (i % 2 == 0):
            res.append(arr[i])
    return res


arr = [1, 2, 3, 4]
arr = [60, 63, 55, 41, 22, 11, 57]
print(getAlternates(arr))
