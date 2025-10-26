# C1
def missingNum_c1(arr):
    check = 0
    sort_arr = sorted(arr)  # O(n log n)
    for i in range(len(arr)):
        check = i + 1
        if (sort_arr[i] != check):
            break
        else:
            check += 1
    return check


# C2
def missingNum_c2(arr):
    sum_i = 0
    for i in range(0, len(arr) + 2):
        sum_i += i

    return sum_i - sum(arr)


arr = [1, 2, 3, 5]
arr = [8, 2, 4, 5, 3, 7, 1]
arr = [1]
# arr = [2, 6, 5, 1, 3]
# arr = [2, 3]
# arr = [1, 2]
print(missingNum_c1(arr))
print(missingNum_c2(arr))
