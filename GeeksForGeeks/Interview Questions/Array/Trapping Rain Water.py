# Cách 1 dùng Prefix và Suffix
def maxWater_c1(arr):
    n = len(arr)
    res = 0
    left = [0] * n
    right = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(1, n - 1):
        check = min(left[i], right[i])
        res += check - arr[i]
    return res


# Cách 2 dùng Two-Pointers
def maxWater_c2(arr):
    left = 1
    right = len(arr) - 2
    l_max = arr[0]
    r_max = arr[-1]
    res = 0

    while left <= right:
        if (r_max <= l_max):
            res += max(0, r_max - arr[right])
            r_max = max(r_max, arr[right])
            right -= 1
        else:
            res += max(0, l_max - arr[left])
            l_max = max(l_max, arr[left])
            left += 1

    return res


arr = [3, 0, 1, 0, 4, 0, 2]
arr = [1, 2, 3, 4]
arr = [2, 1, 5, 3, 1, 0, 4]
print(maxWater_c1(arr))
print(maxWater_c2(arr))
