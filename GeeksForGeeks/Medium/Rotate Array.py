def rotateArr(arr, d):
    if (d < len(arr)):
        arr[:] = arr[d:] + arr[:d]
        return arr[:]
    else:
        step = d % len(arr)
        if (step == 0):
            return arr
        else:
            step = step - len(arr)
            arr[:] = arr[step:] + arr[:step]
            return arr[:]


arr = [1, 2, 3, 4, 5]
d = 2
# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# d = 3
# arr = [7, 3, 9, 1]
# d = 9
arr = [1, 2, 3, 4, 5]
d = 2
print(rotateArr(arr, d))
