# C1
def valueEqualToIndex_c1(arr):
    hash_table = {}
    valueEqualToIndex_list = []
    for i in range(0, len(arr)):
        hash_table[i+1] = hash_table.get(i+1, arr[i])

    for num in hash_table:
        if (num == hash_table.get(num)):
            valueEqualToIndex_list.append(num)
    return valueEqualToIndex_list


# C2
def valueEqualToIndex_c2(arr):
    valueEqualToIndex_list = []
    for i in range(0, len(arr)):
        if (i+1 == arr[i]):
            valueEqualToIndex_list.append(i+1)
    return valueEqualToIndex_list


arr = [15, 2, 45, 4, 7]
arr = [1]
print(valueEqualToIndex_c2(arr))
