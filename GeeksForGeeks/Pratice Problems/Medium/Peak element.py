def peakElement(arr):
    res = []
    n = len(arr)
    if n == 0:
        return res
    if n == 1:
        return [0]

    # thêm phần tử giả 2 bên để tránh check biên
    temp_arr = [arr[0] - 1] + arr + [arr[-1] - 1]

    left = 0
    mid = 1
    right = 2

    while right < len(temp_arr):
        if temp_arr[left] < temp_arr[mid] > temp_arr[right]:
            res.append(mid - 1)

        left += 1
        mid += 1
        right += 1

    return res


arr = [3, 5]
# arr = [1, 2, 4, 5, 7, 8, 3]
# arr = [10, 20, 15, 2, 23, 90, 80]
# arr = [1, 2, 3]
# arr = [-3, -5]
# arr = [8, 5, 10, 8, 7, 6, 1, 3]
arr = [-20, 7, 8, -14, -18, 8, -18, 1, -16, -3]
print(peakElement(arr))
