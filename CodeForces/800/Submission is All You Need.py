import sys
from math import ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    total = sum(nums)
    i = 0
    j = 1
    if (len(nums) == 1 and nums[0] == 0):
        return 0
    if (1 not in Counter(nums)):
        return sum(nums)
    while j < len(nums) - 1:
        if (nums[i] == 0 and nums[j] == 1):
            nums[i] = 1
            i += 1
        if (nums[i] != 0):
            i += 1
        j += 1

    return total if total > sum(nums) else sum(nums)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
