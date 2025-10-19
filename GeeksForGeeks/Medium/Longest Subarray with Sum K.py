def longestSubarray(arr, k):
    res = []
    n = len(arr)
    for r in range(1, n+1):
        for i in range(n - r + 1):
            if (sum(arr[i:i+r]) == k):
                res.append(len(arr[i:i+r]))

    return 0 if res == [] else max(res)


arr = [-5, 8, -14, 2, 4, 12]
k = -5

# arr = [10, -10, 20, 30]
# k = 5

arr = [6, -15, -64, 11, -45, 22, -73, -2, 71,
       7, 6, -15, -64, 11, -45, 22, -73, -2, 71, 7]
k = -14

print(longestSubarray(arr, k))
