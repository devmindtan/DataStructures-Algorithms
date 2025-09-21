import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(len(arr)):
        if (arr[i] == 1):
            sum += 1
    return sum


if __name__ == "__main__":
    t = int(input())
    res = 0
    for _ in range(t):
        x = solve()
        if (x >= 2):
            res += 1
    print(res)
