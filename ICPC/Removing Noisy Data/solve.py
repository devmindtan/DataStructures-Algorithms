import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve_1():
    n = int(input())
    arr = list(map(int, input().split()))

    zero_count = arr.count(0)
    positive = list(filter(lambda x: x > 0, arr))
    negative = list(filter(lambda x: x < 0, arr))

    if (zero_count >= 2):
        print(max(arr), min(arr))
    elif (zero_count == 1):
        print(0, 0)
    else:
        if (len(negative) % 2 == 1):
            to_remove = max(negative)
        else:
            to_remove = min(positive)

        print(to_remove, to_remove)


if __name__ == "__main__":
    solve_1()
