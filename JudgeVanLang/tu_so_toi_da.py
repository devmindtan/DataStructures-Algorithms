
def solve():
    T = int(input())
    for _ in range(T):
        v = list(map(int, input().split()))
        v.sort()
        print(v[0] * v[1] + v[2] * v[3])


solve()
