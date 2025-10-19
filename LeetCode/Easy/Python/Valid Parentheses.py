import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve():
    s = input()
    res = []
    hash_table = {"]": "[", ")": "(", "}": "{"}
    for br in s:
        if br in "[{(":
            res.append(br)
        elif br in "]})":
            if not res or res[-1] != hash_table[br]:
                return False
            res.pop()
    return not res  # Nếu không rỗng, không None, không = 0,...


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
