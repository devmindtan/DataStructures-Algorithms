def sort012(arr):
    check_2 = 0
    check_0 = len(arr) - 1

    for l in range(len(arr)):
        if (arr[l] != 2):
            arr[l], arr[check_2] = arr[check_2], arr[l]
            check_2 += 1
    for r in range(len(arr)-1, -1, -1):
        if (arr[r] != 0):
            arr[r], arr[check_0] = arr[check_0], arr[r]
            check_0 -= 1

    return arr


arr = [0, 1, 2, 0, 1, 2]
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr = [2, 2, 1, 0, 0, 1]

print(sort012(arr))
