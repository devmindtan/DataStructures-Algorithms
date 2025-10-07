import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    for _ in range(k):
        if (n % 10 != 0):
            n = n - 1
        else:
            n = n / 10
    print(int(n))


if __name__ == "__main__":
    solve()
