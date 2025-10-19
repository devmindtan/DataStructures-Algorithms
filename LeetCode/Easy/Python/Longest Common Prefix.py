import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(str, input().split()))
    res = []
    for chars in zip(*arr):
        if len(set(chars)) == 1:
            res.append(chars[0])
        else:
            break
    print("".join(res))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
