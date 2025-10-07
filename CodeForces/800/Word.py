import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = input()
    upper = 0
    lower = 0
    for i in range(len(n)-1):
        if (n[i] == n[i].upper()):
            upper += 1
        else:
            lower += 1
    if (upper > lower):
        print(n.upper())
    else:
        print(n.lower())


if __name__ == "__main__":
    solve()
