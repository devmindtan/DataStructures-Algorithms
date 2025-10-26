def findEquilibrium_c1(arr):
    left = 0
    right = 0
    for i in range(1, len(arr)):
        right += arr[i]

    for i in range(1, len(arr)):
        right -= arr[i]
        left += arr[i-1]
        if (left == right):
            return i
    return -1


def findEquilibrium_c2(arr):
    total = sum(arr)
    left = 0

    for i in range(len(arr)):
        right = total - left - arr[i]
        if left == right:
            return i
        left += arr[i]
    return -1


arr = [1, 2, 0, 3]
arr = [1, 1, 1, 1]
arr = [5]
arr = [0, -3, 3]

print(findEquilibrium_c1(arr))
print(findEquilibrium_c2(arr))
