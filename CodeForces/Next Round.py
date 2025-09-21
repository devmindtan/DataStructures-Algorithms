import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve(n, k):
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if (arr[i] >= arr[k-1] and arr[i] > 0):
            res += 1
    print(res)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = arr[0]
    k = arr[1]
    solve(n, k)
