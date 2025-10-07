# Kadane hoạt động dựa trên nguyên lý rất đơn giản:
# “Nếu tổng hiện tại bị âm, bỏ nó đi và bắt đầu lại từ phần tử tiếp theo.”

# C1
def maxSubarraySum_c1(arr):
    if (len(arr) == 1):
        return arr[0]
    if (len(arr) == 2):
        return max(arr)
    check_odd = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            check_odd += 1
        else:
            break
    if (check_odd == len(arr)):
        return max(arr)
    j = 2
    max_value = max(arr[0] + arr[1], arr[1])
    max_temp = max(arr[0], arr[1])

    while j < len(arr):
        # print(max_temp)
        if (max_temp < max_value):
            max_temp = max_value

        if (max_value > 0):
            max_value += arr[j]
            j += 1
        else:
            max_value = arr[j]
            j += 1

    if (max_value < max_temp):
        return max_temp
    return max_value


# C2
def maxSubarraySum_c2(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# C3
def maxSubarraySum_c3(arr):
    if len(arr) == 0:
        return 0
    if all(x < 0 for x in arr):
        return max(arr)

    max_value = arr[0]
    max_temp = arr[0]

    for j in range(1, len(arr)):
        # hoặc bắt đầu lại từ arr[j] nếu tổng trước âm
        max_value = max(arr[j], max_value + arr[j])
        # lưu kết quả lớn nhất
        max_temp = max(max_temp, max_value)

    return max_temp


arr = [2, 3, -8, 7, -1, 2, 3]
arr = [-2, -4]
# arr = [5, 4, 1, 7, 8]
# arr = [6, -6, 3, -8, 2, 3, 3, -3, -6, 0]
# arr = [3, 7, -9, -10, 4, 4]
arr = [7, -9]
arr = [-1, 25, 25, 18, 18, 2, -8, 6, -17, 20, 8]
# arr = [4, -1, 2, -7, 3, 4]
# arr = [1, 2, -5, 4, -3, 2, 3, -1, 2]
arr = [29, -26, 0, 10, 1]
print(maxSubarraySum_c1(arr))
print(maxSubarraySum_c2(arr))
print(maxSubarraySum_c3(arr))
