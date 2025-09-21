import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(str, input().split()))
    for i in range(len(arr)):
        char = arr[i]
        if (len(char) > 10):
            print(f"{char[0]}{len(char[1:-1])}{char[-1]}")
        else:
            print(char)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
