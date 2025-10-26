def removeDuplicates(arr):
    seen = set()
    sub_arr = []
    for num in arr:
        if (num not in seen):
            sub_arr.append(num)
            seen.add(num)
    return sub_arr


def removeDuplicates(arr):
    sub_arr = [arr[0]]
    for i in range(1, len(arr)):
        if (arr[i] != arr[i - 1]):
            sub_arr.append(arr[i])
    return sub_arr


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(removeDuplicates(arr))
