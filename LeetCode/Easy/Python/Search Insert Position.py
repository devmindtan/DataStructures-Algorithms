from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if (nums[mid] == target):
            return mid
        if (target > nums[mid]):
            left = mid + 1
        else:
            right = mid - 1
    if (target < nums[mid]):
        return mid
    else:
        return mid + 1


nums = [1, 3, 5, 6]
target = 5
nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))
