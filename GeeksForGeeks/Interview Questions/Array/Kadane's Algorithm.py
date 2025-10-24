# Tổng lớn nhất của một dãy con liên tiếp (maximum subarray sum) trong một mảng số (có thể chứa cả số âm).
'''
Ý tưởng của Kadane:
    Ở mỗi phần tử, ta chỉ cần biết tổng lớn nhất của dãy con kết thúc tại vị trí đó.
'''


def maxSubarraySum(arr):
    maxEnding = arr[0]
    maxSoFar = arr[0]

    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])

        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


arr = [2, 3, -8, 7, -1, 2, 3]
# arr = [-2, -4]
# arr = [5, 4, 1, 7, 8]
# arr = [-3, -2, -6, -1, -7, -4]
# arr = [6, -6, 3, -8, 2, 3, 3, -3, -6, 0]
arr = [-1, 25, 25, 18, 18, 2, -8, 6, -17, 20, 8]
arr = [-4, 12, -12, -24, -7, -1, -9, -30, -5, 14, 25, 17, -26, 8, -7, -10]
print(maxSubarraySum(arr))
