def solve():
    t = int(input())
    results = []

    target_seconds = 12 * 3600
    day_seconds = 24 * 3600

    for _ in range(t):
        h, m, s = map(int, input().split())

        current_seconds = h * 3600 + m * 60 + s

        diff = target_seconds - current_seconds

        if diff <= 0:
            diff += day_seconds

        results.append(str(diff))

    return results


def main():
    for n in solve():
        print(n)


main()
