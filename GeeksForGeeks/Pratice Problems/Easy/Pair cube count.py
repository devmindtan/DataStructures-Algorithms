from math import cbrt


def pairCubeCount_c1(n):
    arr_x = []
    arr_y = []
    check = 0
    if (n <= 1):
        return 1
    for i in range(1, int(n**(1/3))+1):
        x = i ** 3
        y = (int(n**(1/3)+1)-i) ** 3
        arr_x.append(x)
        arr_y.append(y)
    for i in range(len(arr_x)):
        for j in range(len(arr_y)):
            res = arr_x[i] + arr_y[j]
            if (res == n):
                check += 1
                break
    return check


def pairCubeCount_c2(n):
    # a^3 + b^3 = n
    check = 0
    res = 0
    for i in range(1, int(cbrt(n))+1):
        b = int(cbrt(n - (i**3)))
        res = b**3 + i**3
        # print(res)
        if (res == n):
            # print(b, i)
            check += 1

    return check


n = 9
# n = 16
# n = 5002
n = 1729
# n = 1
# n = 1674
# print(pairCubeCount_c1(n))

print(pairCubeCount_c2(n))

# print(n**(1/3))
# print(7**3)
# print(10**3 + 9**3)
print(int(n**(1/3)))
print(int(cbrt(n)))
