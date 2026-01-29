# Thuat toan KMP
def solve():
    t = int(input())
    res = []

    for _ in range(t):
        s, c = list(input().split())

        n, m = len(s), len(c)

        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if c[i] == c[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        check = 0
        i = 0
        j = 0
        while i < n:
            if s[i] == c[j]:
                i += 1
                j += 1

            if j == m:
                check += 1
                j = lps[j - 1]
            elif i < n and s[i] != c[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        res.append(check)

    return res


def main():
    for n in solve():
        print(n)


main()
