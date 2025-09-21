import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve(str):
    if (len(set(str)) % 2 == 0):
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


if __name__ == "__main__":
    str = input().strip()
    print(solve(str))
