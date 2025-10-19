from typing import List


def removeElement(nums: List[int], val: int) -> int:
    check = 0
    i = 0
    j = len(nums) - 1
    while (i <= j):
        if (nums[i] == val):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        else:
            i += 1
            check += 1

        if (nums[j] == val):
            j -= 1

    return check


# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
# nums = [3, 2, 2, 3]
# val = 3
nums = list(map(int, input().split()))
val = int(input())
print(removeElement(nums, val))
