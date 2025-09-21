import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(str, input().split()))
    x = 0
    for i in range(len(arr)):
        if (arr[i] == "++X" or arr[i] == "X++"):
            x = 1
        elif (arr[i] == "X--" or arr[i] == "--X"):
            x = -1
    return x


if __name__ == "__main__":
    t = int(input())
    res = 0
    for _ in range(t):
        x = solve()
        res += x
    print(res)
