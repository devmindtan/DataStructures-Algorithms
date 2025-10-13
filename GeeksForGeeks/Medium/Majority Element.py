def majorityElement(arr):
    hash_table = {}
    for num in arr:
        hash_table[num] = hash_table.get(num, 0) + 1

    check = 0
    for i in range(len(arr)):
        if (hash_table.get(arr[i]) > len(arr)/2):
            check = arr[i]

    return -1 if check == 0 else check


arr = [1, 1, 2, 1, 3, 5, 1]
# arr = [7]
# arr = [2, 13]
print(majorityElement(arr))
