def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]
    print(prefProduct)

    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]
    print(suffProduct)

    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res


def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    # Prefix (chay thuận chiều)
    for i in range(1, n):
        prefProduct[i] = prefProduct[i - 1] * arr[i - 1]

    # Suffix (chạy ngược chiều)
    for i in range(n - 2, -1, -1):
        suffProduct[i] = suffProduct[i + 1] * arr[i + 1]

    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]
    return res


arr = [10, 3, 5, 6, 2]
# arr = [12, 0]
print(productExceptSelf(arr))
