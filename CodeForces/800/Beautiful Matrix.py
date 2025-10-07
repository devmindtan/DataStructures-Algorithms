import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline

# C1 (Cách làm ban đầu)
# def solve():
#     matrix = [list(map(int, input().split())) for _ in range(5)]
#     resI = 0
#     resJ = 0
#     step = 0
#     for i in range(5):
#         for j in range(5):
#             if (matrix[i][j] == 1):
#                 resI = i
#                 resJ = j
#     while (resI != 2 or resJ != 2):
#         if (resI < 2):
#             resI = resI + 1
#             step += 1
#         elif (resI > 2):
#             resI = resI - 1
#             step += 1
#         if (resJ < 2):
#             resJ = resJ + 1
#             step += 1
#         elif (resJ > 2):
#             resJ = resJ - 1
#             step += 1

#     if (resI == 2 and resJ == 2):
#         return step


# C2 (Khoảng cách Manhattan)
def solve():
    matrix = [list(map(int, input().split())) for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if (matrix[i][j] == 1):
                return abs(i - 2) + abs(j - 2)


if __name__ == "__main__":
    print(solve())
