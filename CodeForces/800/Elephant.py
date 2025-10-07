import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    n = int(input())
    res = 0
    step = 5
    while True:
        if (n > 5):
            step += 5
            res += 1
            if (step > n):
                res += 1
                break
            elif (step == n):
                res += 1
                break
        else:
            res = 1
            break
    print(res)
    # C2 print(math.ceil(12/5))


if __name__ == "__main__":
    solve()
