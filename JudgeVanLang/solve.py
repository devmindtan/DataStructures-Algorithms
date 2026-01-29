def solve():
    t = int(input())
    res = []

    for _ in range(t):
        # nums = list(map(int, input().split()))
        nums = map(int, input().split())
        hash = {}
        sample = {0: 1, 2: 2, 6: 1}
        for i, v in enumerate(nums):
            # print(i, v)
            if v != 0:
                hash[i] = v
        total = 0
        for i in sample:
            sample[i] = sample.get(i, 0) - hash.get(i, 0)
            hash[i] = hash.get(i, 0) - sample.get(i, 0)
        res.append(hash)

    return res


def main():
    for n in solve():
        print(n)


main()

# s = "abaaaaba"
# c = "aa"
# pos = s.find(c, 4)
# print(pos)

# def solve():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     dp = [1] * n
#     for i in range(1, n):
#         for j in range(i):
#             if arr[j] < arr[i]:
#                 if dp[j] + 1 > dp[i]:
#                     dp[i] = dp[j] + 1
#     print(max(dp))


# solve()
