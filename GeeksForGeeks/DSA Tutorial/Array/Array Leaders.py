def leaders(arr):
    res = []
    res.append(arr[-1])
    cur = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        cur = max(cur, arr[i])
        if (arr[i] == cur):
            res.append(cur)

    return res[::-1]


arr = [16, 17, 4, 3, 5, 2]
arr = [10, 4, 2, 4, 1]
print(leaders(arr))
