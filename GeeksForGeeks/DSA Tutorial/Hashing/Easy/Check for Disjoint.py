def areDisjoint(a, b):
    set_a = set(a)
    for num in b:
        if (num in set_a):
            return False
    return True


a = [2, 34, 11, 9, 3]
b = [2, 1, 3, 5]

a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 5]
print(areDisjoint(a, b))
