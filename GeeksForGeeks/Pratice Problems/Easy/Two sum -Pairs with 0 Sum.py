def for_custom(l, r):
    return for i


def getPairs(arr):
    arr.sort()
    pos = {}
    neg = {}
    res = []
    zero = 0
    for num in arr:
        if (num > 0):
            pos[num] = pos.get(num, 0) + 1
        elif (num < 0):
            neg[num] = neg.get(num, 0) + 1
        else:
            zero += 1
    for num in neg:
        if (-num in pos):
            res.append([num, -num])

    if (zero > 1):
        res.append([0, 0])

    return res


arr = [-1, 0, 1, 2, -1, -4]
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
arr = [0, 0, 0]
print(getPairs(arr))
