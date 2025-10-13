def twoSum_c1(nums, target):  # Thủ công
    hash_table = {}
    res = {}
    for i in range(len(nums)):
        hash_table[i] = hash_table.get(i, nums[i])

    for k, v in hash_table.items():
        temp = target - v
        if (temp in res):
            return [res[temp], k]
        res[v] = k
    return res


def twoSum_c2(nums, target):  # Sử dụng enumerate
    res = {}
    for k, v in enumerate(nums):
        temp = target - v
        if (temp in res):
            return [res[temp], k]
        res[v] = k
    return res


nums = [11, 15, 3, 7, 2]
target = 9
# nums = [3, 2, 4]
# target = 6
# nums = [3, 3]
# target = 6
print(twoSum_c1(nums, target))
print(twoSum_c2(nums, target))
# print(f"{2**64:,}")
