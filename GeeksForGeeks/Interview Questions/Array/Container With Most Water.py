def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)

        if (arr[left] > arr[right]):
            right -= 1
        else:
            left += 1

    return res


arr = [1, 5, 4, 3]
arr = [3, 1, 2, 4, 5]
arr = [2, 1, 8, 6, 4, 6, 5, 5]
arr = [4, 7, 6, 10, 3, 9, 1]
print(maxWater(arr))
