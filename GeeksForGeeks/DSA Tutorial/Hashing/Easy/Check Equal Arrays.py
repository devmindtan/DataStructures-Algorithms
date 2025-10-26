def checkEqual(a, b):
    hash_table = {}

    for num in a:
        hash_table[num] = hash_table.get(num, 0) + 1

    for num in b:
        if (num not in hash_table):
            return False
        if (hash_table[num] == 0):
            return False
        hash_table[num] -= 1
    return True


a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]

a = [1, 2, 5]
b = [2, 4, 15]
print(checkEqual(a, b))
