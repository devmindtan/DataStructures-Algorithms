import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve_1(n, m):
    students = [list(map(int, input().strip())) for _ in range(n)]
    pair_list = []
    max_pair = []
    count = 0
    # pair = [min(x + y, 1) for x, y in zip(a, b)]

    for i in range(n):
        for j in range(i+1, n):
            pair = [min(x + y, 1) for x, y in zip(students[i], students[j])]
            pair_list.append(pair)

    for i in range(len(pair_list)):
        max_pair.append(sum(pair_list[i]))

    for i in range(len(max_pair)):
        if (max_pair[i] == max(max_pair)):
            count += 1

    print(max(max_pair), count)


def solve_2(n, m):
    students = [list(map(int, input().strip())) for _ in range(n)]
    max_topics = 0
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            total = sum(x or y for x, y in zip(students[i], students[j]))
            if total > max_topics:
                max_topics = total
                count = 1
            elif total == max_topics:
                count += 1

    print(max_topics)
    print(count)


if __name__ == "__main__":
    n, m = map(int, input().split())
    # solve_1(n, m)
    solve_2(n, m)
