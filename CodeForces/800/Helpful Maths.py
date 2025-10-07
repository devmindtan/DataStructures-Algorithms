import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve(str):
    print("+".join(sorted(str.split("+"))))


if __name__ == "__main__":
    str = input().strip()
    solve(str)
