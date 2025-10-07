def subarraySum(arr, target):
    i = 0
    j = 1
    prefix = arr[0]
    while i <= j and j <= len(arr):
        if (prefix < target):
            if (j > len(arr) - 1):
                return [-1]
            prefix += arr[j]
            j += 1
        elif (prefix > target):
            prefix -= arr[i]
            i += 1
        else:
            return [i+1, j]
    return [i+1, j] if prefix == target else [-1]


# arr = [1, 2, 3, 7, 5]
# target = 12

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 15

# arr = [12, 18, 5, 11, 30, 5]
# target = 69

# arr = [19, 23, 15, 6, 6, 2, 28, 2]
# target = 2

# arr = [38, 22, 20, 12, 47, 23, 18, 13, 18, 47, 36, 42]
# target = 174

# arr = [26, 3, 28, 7]
# target = 52

print(subarraySum(arr, target))
