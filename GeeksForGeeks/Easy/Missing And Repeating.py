def findTwoElement(arr):
    hash_table = {}
    dup = 0
    for i in range(len(arr)):
        hash_table[arr[i]] = hash_table.get(arr[i], 0) + 1
    for num in hash_table:
        if (hash_table[num] == 2):
            dup = num
            break

    mis = sum(range(len(arr)+1)) - sum(hash_table)

    return [dup, mis]


arr = [2, 2]
# arr = [4, 3, 6, 2, 1, 1]
arr = [1, 3, 3]
print(findTwoElement(arr))
