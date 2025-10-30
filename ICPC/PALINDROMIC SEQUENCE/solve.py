def solve():
    M, N = map(int, input().split())
    p, q = map(int, input().split())

    if ((p == M and q == N) or (p == 1 and q == 1) or (p == 1 and q == N) or (p == M and q == 1)):
        return 3
    elif (p > 1 and q == 1) or (p == 1 and q > 1) or (p > 1 and q == N):
        return 5
    else:
        return 8


print(solve())
