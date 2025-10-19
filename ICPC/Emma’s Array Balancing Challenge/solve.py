import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve_1():
    a = map(int, input().split())
    arr = list(map(int, input().split()))

    mid = len(arr)//2
    res = 0
    left = 0
    right = 0
    for i in range(len(arr)):
        if (i <= mid):
            left += arr[i]
        else:
            right += arr[i]

    res = abs(right - left)

    print(res)


if __name__ == "__main__":
    solve_1()
