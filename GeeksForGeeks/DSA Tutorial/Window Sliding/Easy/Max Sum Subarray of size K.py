def maxSubarraySum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        print(i)
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [100, 200, 300, 400]
k = 2

# arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4

# arr = [100, 200, 300, 400]
# k = 1
print(maxSubarraySum(arr, k))
