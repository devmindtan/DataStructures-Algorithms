from math import sqrt


def threeDivisors(self, query, q):
    gcd_list = [[] for _ in range(q)]
    for i in range(len(query)):
        num = query[i]
        for j in range(1, num + 1):
            if (self.exactly_3_div(j)):
                gcd_list[i].append(j)

    return [len(sup) for sup in gcd_list]


def is_prime(n):
    if (n < 2):
        return False
    else:
        for i in range(2, int(sqrt(n)+1)):
            if (n % i == 0):
                return False
        return True


def exactly_3_div(n):
    _sqrt = int(sqrt(n))
    if (n < 4):
        return False

    if _sqrt * _sqrt != n:
        return False

    if (is_prime(_sqrt)):
        return True
    else:
        return False


q = 3
query = [8468, 6335, 6501]
# query = [5]
# arr = [[]]
# arr[0].append(1)
# print(arr)
print(threeDivisors(query, q))
# print(exactly_3_div(9))
