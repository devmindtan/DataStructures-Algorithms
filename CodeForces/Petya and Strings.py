import heapq
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque
import math
import sys

input = sys.stdin.readline


def solve(str1, str2):
    for i in range(len(str1)):
        if (str1[i].lower() < str2[i].lower()):
            return -1
        elif (str1[i].lower() > str2[i].lower()):
            return 1
    return 0


if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(solve(str1, str2))
