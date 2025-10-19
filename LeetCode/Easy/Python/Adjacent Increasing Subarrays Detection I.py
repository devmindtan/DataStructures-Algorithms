from typing import List


def hasIncreasingSubarrays(nums: List[int], k: int) -> bool:
    i = 0
    j = k
    check = 0
    while j < len(nums) - 1:
        if (check == k-1):
            return True
        if (nums[i] < nums[i+1] and nums[j] < nums[j+1]):
            check += 1
        if (nums[i] > nums[i+1] or nums[j] > nums[j+1]):
            check = 0
        i += 1
        j += 1
    return True if check == k-1 else False


nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
k = 3
# nums = [5, 8, -2, -1]
# k = 2
print(hasIncreasingSubarrays(nums, k))
