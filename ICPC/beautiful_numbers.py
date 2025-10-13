import sys
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
import heapq

input = sys.stdin.readline


def solve_1():
    a, b = map(int, input().split())
    arr = []
    arr_th2 = []
    arr_1 = []
    arr_2 = []
    test = 0
    hash_table = {}
    check_case = {}
    res = {}
    check = 0

    if b <= 10:
        for i in range(a, b + 1):
            if i * 3 < b:
                arr_1.append(i * 3)
            if i * 2 < b:
                arr_2.append(i * 2)
        common = set(arr_1) & set(arr_2)
        for num in common:
            res[num] = 2
    else:
        for i in range(a, b + 1):
            lst = list(map(int, str(i)))
            hash_table[i] = sum(lst)
            th1 = list(map(int, str(i - sum(lst))))
            arr.append(sum(th1))
            test = sum(th1)

        for num in hash_table:
            if hash_table[num] == test:
                check_case[num] = 1
                res[num] = test

        for k, v in res.items():
            for i in range(v, 0, -1):
                val = k - i * 2
                if val >= 0:
                    th2 = list(map(int, str(val)))
                    arr_th2.append(sum(th2))
            for num in arr_th2:
                if num == res[k]:
                    res[k] = 2

    for num in res:
        if res[num] == 2:
            check += 1

    print(check)


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        solve_1()
