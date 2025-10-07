import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    if n % 2 == 0 and n > 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
