from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    j = 0
    for i in range(m+n):
        if (nums1[i] == 0 and j < len(nums2)):
            nums1[i] = nums2[j]
            j += 1
    nums1.sort()
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))
