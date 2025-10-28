from collections import Counter
from math import factorial as f


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    check = 0
    count = dict(Counter(arr))
    for num in count:
        if (count[num] >= 2):
            check += int(f(count[num]) / (f(2) * f(count[num] - 2)))

    return check


print(solve())
