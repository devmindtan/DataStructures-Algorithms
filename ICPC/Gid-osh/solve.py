def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        if len(arr) <= 2:
            print(0)
            continue

        res = min(arr[-1] - arr[1], arr[-2] - arr[0])
        print(res)


solve()
