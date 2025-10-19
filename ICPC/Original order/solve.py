import heapq
from bisect import bisect_left, bisect_right
import math
import sys

input = sys.stdin.readline


def solve_1():
    n = int(input())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Tính nghịch đảo của A và C
    invA = [0] * n
    invC = [0] * n

    for i in range(n):
        print(i)
        invA[A[i] - 1] = i + 1
        invC[C[i] - 1] = i + 1

    # B[i] = C⁻¹[A⁻¹[i]]
    B = [0] * n
    for i in range(n):
        B[i] = invC[invA[i] - 1]

    print(*B)


def solve_2():
    n = int(input())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * n
    invA = {}
    invC = {}
    for i in range(n):
        invA[A[i]] = i+1
        invC[C[i]] = i+1
    dict(sorted(invA.items()))
    dict(sorted(invC.items()))

    for i in range(n):
        B[i] = invC[invA[i+1]]
    return B


if __name__ == "__main__":
    # solve_1()
    print(*solve_2())
