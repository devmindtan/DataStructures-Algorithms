from typing import List


def removeDuplicates_c1(nums: List[int]) -> int:
    remove_dup = sorted(list(set(nums)))
    nums[:] = []
    for num in remove_dup:
        nums.append(num)
    check = len(remove_dup)
    return check, nums


def removeDuplicates_c2(nums: List[int]) -> int:
    check = 0
    for i in range(len(nums) - 1):
        if (nums[i] == nums[i+1]):
            nums[i] = float("inf")
    nums.sort()
    check = len(list(filter(lambda x: x != float("inf"), nums)))
    return check, nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [-1, 0, 0, 0, 0, 3, 3]
print(removeDuplicates_c1(nums))
