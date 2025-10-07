import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    arr = list(map(int, input().strip()))
    count_lucky_number = 0
    for x in arr:
        if (x == 4):
            count_lucky_number += 1
        if (x == 7):
            count_lucky_number += 1
    if (count_lucky_number == 4 or count_lucky_number == 7):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
