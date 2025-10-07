# C1 - O(n^2) + O(m log m) - Dùng vòng lặp thủ công
def check_elements_c1(arr, n, A, B):
    _arr = sorted(set(arr))
    check = 0
    for i in range(A, B+1):
        for j in range(len(_arr)):
            if (_arr[j] == i):
                check += 1
                break
    return check == (B-A) + 1


# C2 - O(n + (B-A + 1)) - HashTable (dùng set trong python tạo biến check để lưu kết quả)
def check_elements_c2(arr, n, A, B):
    unique = set(arr)
    check = 0
    for i in range(A, B+1):
        if (i in unique):
            check += 1
    return check == B-A+1


# C3 - O(n + (B-A + 1)) - HashTable (dùng set trong python không dùng biến check)
def check_elements_c3(arr, n, A, B):
    unique = set(arr)
    for i in range(A, B+1):
        if (i not in unique):
            return False
    return True


# C3 - O(n + (B-A + 1)) - HashTable (dùng kiểu dữ liệu dict trong python - thủ công)
def check_elements_c4(arr, n, A, B):
    hash_table = {}

    for num in arr:
        hash_table[num] = True

    for i in range(A, B+1):
        if (i not in hash_table):
            return False
    return True

# n = 7
# A = 2
# B = 5
# arr = [1, 4, 5, 2, 7, 8, 3]


# n = 7
# A = 2
# B = 6
# arr = [1, 4, 5, 2, 7, 8, 3]

n = 16
A = 5
B = 8
# arr = [1, 9, 1, 1, 5, 8, 9, 4, 3, 8, 10, 9, 4, 1,
#        8, 2, 6, 5, 1, 8, 5, 2, 6, 8, 2, 8, 9, 5, 10]
# arr = [1, 1, 8, 8, 5, 5, 9, 3, 9, 4, 6, 7, 5, 5, 5, 6, 1, 8, 4, 9, 3, 5, 4, 4]
arr = [6, 3, 2, 10, 5, 6, 4, 4, 9, 3, 7, 9, 9, 9, 6, 4]
print(check_elements_c1(arr, n, A, B))
print(check_elements_c2(arr, n, A, B))
print(check_elements_c3(arr, n, A, B))
print(check_elements_c4(arr, n, A, B))
