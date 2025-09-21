import heapq
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque
import math
import sys

input = sys.stdin.readline


def solve(str):
    firstLetter = str[0].upper()
    print(firstLetter+str[1:])


if __name__ == "__main__":
    str = input().strip()
    solve(str)
