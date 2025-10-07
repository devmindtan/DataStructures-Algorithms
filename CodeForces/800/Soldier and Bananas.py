import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    k, n, w = map(int, input().split())
    res = 0
    sum = 0
    for i in range(w+1):
        sum += i
    if (n < k*sum):
        res = k*sum - n
    else:
        res = 0
    print(res)


if __name__ == "__main__":
    solve()
