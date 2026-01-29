def solve():
    t = int(input())
    res = []

    for _ in range(t):
        # nums = list(map(int, input().split()))
        nums = input()
        check = 1
        out = 1
        n = len(nums)
        for i in range(0, n - 1):
            if nums[i + 1] > nums[i]:
                check += 1
            else:
                check = 1
            out = max(out, check)
        res.append(out)

    return res


def main():
    for n in solve():
        print(n)


main()
