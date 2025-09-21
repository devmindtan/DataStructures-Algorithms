import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    cur = 0
    cap = 0
    for _ in range(n):
        a, b = map(int, input().split())
        cur -= a      # người xuống trước
        cur += b      # người lên sau
        cap = max(cap, cur)

    print(cap)


if __name__ == "__main__":
    solve()
