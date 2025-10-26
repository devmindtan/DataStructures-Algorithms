def isSubset_c1(a, b):
    c = b[:]
    dp = []
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == c[j]):
                dp.append(c[j])
                c[j] = None
                break
    return len(dp) == len(c)


def isSubset_c2(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = 0
    j = 0
    check = 0
    while i <= len(b) - 1 and j <= len(a) - 1:
        if (a[j] == b[i]):
            i += 1
            j += 1
            check += 1
        else:
            j += 1
    return check == len(b)


# a = [11, 7, 1, 13, 21, 3, 7, 3]
# b = [11, 3, 7, 1, 7]
# a = [1, 2, 3, 4, 4, 5, 6]
# b = [1, 2, 4]
a = [10, 5, 2, 23, 19]
b = [19, 5, 3]


# print(len(dp) == c)
# print(len(dp))
# print(c)


print(isSubset_c1(a, b))
print(isSubset_c2(a, b))
