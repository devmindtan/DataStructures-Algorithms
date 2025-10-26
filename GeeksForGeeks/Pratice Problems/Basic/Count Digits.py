def evenlyDivides(n):
    hash_table = {}
    string = str(n)
    check = 0
    for i in range(len(string)):
        if (string[i] != "0"):
            hash_table[i] = hash_table.get(i, int(string[i]))
    for num in hash_table:
        if (n % hash_table[num] == 0):
            check += 1
    return check


n = 2446
n = 12
n = 23
n = 20
print(evenlyDivides(n))
