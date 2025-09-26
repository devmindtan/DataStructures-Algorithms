import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    res = 0
    a, b = map(int, input().split())
    if (a <= b | a, b >= 1 | a, b <= 10):
        while a <= b:
            a = a * 3
            b = b * 2
            res += 1

    print(res)


if __name__ == "__main__":
    solve()
