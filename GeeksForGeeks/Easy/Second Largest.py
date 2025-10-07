def getSecondLargest_c1(arr):
    lar_1 = lar_2 = 0
    i = 0
    j = 0
    temp = arr[:]
    if (len(arr) == 1):
        return -1

    while i < len(arr):
        if (lar_1 < arr[i]):
            lar_1 = arr[i]
        i += 1
    while j < len(arr):
        if (temp[j] == lar_1):
            temp[j] = 0
        if (lar_2 < temp[j]):
            lar_2 = temp[j]
        j += 1
    return -1 if lar_2 == 0 else lar_2


def getSecondLargest_c2(arr):
    first = second = 0
    if (len(arr) == 1):
        return -1

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return -1 if second == 0 else second


arr = [12, 35, 1, 10, 34, 1]
# arr = [10, 5, 10]
# arr = [10, 10, 10]
# arr = [28078, 19451, 935, 28892, 2242, 3570, 5480, 231]
print(getSecondLargest_c1(arr))
print(getSecondLargest_c2(arr))
