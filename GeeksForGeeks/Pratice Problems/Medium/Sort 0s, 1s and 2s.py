# C1 - merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    # Trộn hai mảng con đã sắp xếp
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Gộp phần còn lại (nếu có)
    result += left[i:]
    result += right[j:]
    return result


# C2
def sort012_c2(arr):
    s_i = []
    s_j = []
    s_z = []
    for i in range(len(arr)):
        if (arr[i] == 0):
            s_i.append(arr[i])
        elif (arr[i] == 1):
            s_j.append(arr[i])
        elif (arr[i] == 2):
            s_z.append(arr[i])
    temp = s_i + s_j + s_z
    for i in range(len(arr)):
        arr[i] = temp[i]

    return arr


# C3 - 3 pointers
def sort012_c3(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if (arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif (arr[mid] == 1):
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# arr = [38, 27, 43, 3, 9, 82, 10]
arr = [0, 1, 2, 0, 1, 2]
arr = [2, 1, 2, 2, 2, 1, 0]
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# arr = [10, 2, 20, 3, 5]
print(merge_sort(arr))
print(sort012_c2(arr))
print(sort012_c3(arr))
