from math import factorial as f


def factorial(n):
    res = [int(num) for num in str(f(n))]
    return res


n = 5
print(factorial(n))
