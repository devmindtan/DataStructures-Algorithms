# C1
def closestNumber_c1(n, m):
    dp = []
    res = 0
    x = abs(n)

    if (m > abs(n) and n < 0):
        res = 0
    else:
        for i in range(abs(n), 0, -1):
            if (i % abs(m) == 0):
                dp.append(i)
                break
            elif (i <= m):
                dp.append(0)
                break
        while True:
            if (x % m == 0):
                dp.append(x)
                break
            x += 1

        res1 = 0
        res2 = 0
        if (len(dp) == 2):
            res1 = abs(dp[0] - abs(n))
            res2 = dp[1] - abs(n)
            if (res1 < res2):
                res = dp[0]
            elif (res1 > res2):
                res = dp[1]
            else:
                res = max(dp[0], dp[1])
            if n < 0:
                res = -res
        else:
            if (n > 0):
                res = dp[0]
            elif (n == 0):
                res = 0
            else:
                res = -dp[0]
    return res


# C2
def closestNumber_c2(n, m):
    q = n // m
    n1 = q * m
    n2 = (q + 1) * m

    d1 = abs(n - n1)
    d2 = abs(n - n2)

    if (d1 > d2):
        return n2
    if (d1 < d2):
        return n1
    return n1 if abs(n1) > abs(n2) else n2
