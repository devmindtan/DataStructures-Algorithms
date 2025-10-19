from typing import List


def maxIncreasingSubarrays(nums: List[int]) -> int:
    i = 0
    j = 0
    res = []
    arr = []
    if (len(nums) <= 3):
        return 1
    while j < len(nums) - 1:
        if (j == len(nums) - 1):
            arr.append(len(nums[i:j+1]))
        if (nums[j] < nums[j+1]):
            j += 1
            print(j)
        else:
            j += 1
            i = j
    if (max(arr) == len(nums)):
        return max(arr) // 2
    for i in range(len(arr)):
        if (max(arr) >= 2 and len(arr) > 1):
            if (max(arr) % 2 != 0):
                min = arr[0]
                if (min > arr[i]):
                    min = arr[i]
                    res.append(min)
            else:
                return max(arr) // 2
        else:
            return max(arr)

    return max(res)


nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
# nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
# nums = [5, 8, -2, -1]
# nums = [19, -14, 0, 9]
# nums = [-3, -19, -8, -16]
# nums = [-15, -13, 4, 7]
print(maxIncreasingSubarrays(nums))
