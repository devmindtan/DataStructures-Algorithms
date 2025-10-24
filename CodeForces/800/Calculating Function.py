import sys
from math import ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    if (n % 2 == 0):
        print(n//2)
    else:
        print(-ceil(n/2))


if __name__ == "__main__":
    solve()
