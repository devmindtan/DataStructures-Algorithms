def getSecondLargest(arr):
    l1 = max(arr)
    tmp = [num for num in arr if num != l1]
    return max(tmp) if len(tmp) > 0 else -1


def getSecondLargest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else -1


arr = [12, 35, 1, 10, 34, 1]
arr = [10, 5, 10]
# arr = [10, 10, 10]
print(getSecondLargest(arr))
