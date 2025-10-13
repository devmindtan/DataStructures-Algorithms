def binarysearch(arr, k):
    left, right = 0, len(arr) - 1
    result = -1  # để lưu vị trí nhỏ nhất tìm được

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            result = mid          # lưu vị trí hiện tại
            right = mid - 1       # tiếp tục tìm bên trái
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return result


arr = [1, 2, 3, 4, 5]
k = 4
arr = [11, 22, 33, 44, 55]
k = 445
# arr = [1, 1, 1, 1, 2]
# k = 1
print(binarysearch(arr, k))
