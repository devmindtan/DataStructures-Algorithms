import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    s = input()
    res = 0
    for i in range(n - 1):
        if (s[i] == s[i + 1]):
            res += 1
    print(res)


if __name__ == "__main__":
    solve()
