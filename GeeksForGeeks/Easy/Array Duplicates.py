def findDuplicates(arr):
    hash_table = {}
    findDuplicates_list = []
    for num in arr:
        hash_table[num] = hash_table.get(num, 0) + 1
    for num in hash_table:
        if (hash_table.get(num) == 2):
            findDuplicates_list.append(num)

    return findDuplicates_list


arr = [2, 3, 1, 2, 3]
arr = [3, 1, 2]
print(findDuplicates(arr))
