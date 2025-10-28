'''
weight
intelligence
market value

p = dog 1
q = dog 2

weight p > weight q and intel p >= intel q

*Task:
maximun total money earned
'''


def solve():
    t = int(input())
    all_dogs = [0] * t
    for i in range(t):
        w, e, v = map(int, input().split())
        all_dogs[i] = w, e, v
    all_dogs.sort(reverse=True)

    max_price = 0
    for i in range(len(all_dogs)):
        for j in range(i+1, len(all_dogs)):
            if (all_dogs[i][0] > all_dogs[j][0] and all_dogs[i][1] >= all_dogs[j][1]):
                cur = all_dogs[i][2] + all_dogs[j][2]
                if (max_price < cur):
                    max_price = cur

    return max_price


# print(solve())


def solve():
    n = int(input())
    dogs = []
    for _ in range(n):
        w, e, v = map(int, input().split())
        dogs.append((w, e, v))

    dogs.sort()

    dp = [0] * n
    for i in range(n):
        dp[i] = dogs[i][2]
        print(dp[i], end=" ")
        for j in range(i):
            if dogs[j][1] <= dogs[i][1]:
                dp[i] = max(dp[i], dp[j] + dogs[i][2])

    print(max(dp), dp)


solve()
