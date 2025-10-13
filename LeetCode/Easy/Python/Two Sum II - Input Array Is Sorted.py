def twoSum(nums, target):  # Thủ công
    hash_table = {}
    res = {}
    for i in range(len(nums)):
        hash_table[i+1] = hash_table.get(i+1, nums[i])

    for k, v in hash_table.items():
        temp = target - v
        if (temp in res):
            return [res[temp], k]
        res[v] = k
    return hash_table


nums = [11, 15, 3, 7, 2]
target = 9
# nums = [3, 2, 4]
# target = 6
# nums = [3, 3]
# target = 6
print(twoSum(nums, target))
