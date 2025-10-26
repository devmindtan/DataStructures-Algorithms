def isSubset(a, b):
    hash_a = {}
    hash_b = {}

    for num in a:
        hash_a[num] = hash_a.get(num, 0) + 1

    for num in b:
        hash_b[num] = hash_b.get(num, 0) + 1

    for num in hash_b:
        if (num not in hash_a):
            return False
        if (hash_b[num] > hash_a[num]):
            return False
    return True


a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

# a = [10, 5, 2, 23, 19]
# b = [19, 5, 3]
print(isSubset(a, b))
