def solve():
    t = int(input())
    res = []

    for _ in range(t):
        n, m, k = map(int, input().split())
        formular = (n // k) * (m // k)
        res.append(formular)

    return res


def main():
    for n in solve():
        print(n)


main()
