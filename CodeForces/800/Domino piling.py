import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(int, input().split()))
    res = 1
    for i in range(2):
        if (arr[i] <= 16 and arr[i] > 0):
            if (arr[0] <= arr[1]):
                res = (arr[0] * arr[1]) // 2
    print(res)


if __name__ == "__main__":
    solve()
