def leaders(arr):
    leaders_list = []
    max_right = arr[-1]  # phần tử cuối luôn là leader
    leaders_list.append(max_right)

    # Duyệt ngược lại
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders_list.append(arr[i])
        print(max_right)
    return leaders_list[::-1]  # đảo ngược lại để theo thứ tự ban đầu


# arr = [16, 17, 4, 3, 5, 2]
# arr = [10, 4, 2, 4, 1]
# arr = [5, 10, 20, 40]
# arr = [30, 10, 10, 5]
# arr = [53, 32, 9, 55, 64, 59, 65, 90]
arr = [42, 73, 34, 44, 70, 41, 56]
arr = [20, 54, 25, 14, 38, 63, 14, 72, 11,
       62, 16, 72, 26, 69, 69, 61, 15, 41, 13]

# arr[:3] = [0] * 3
# print(arr)
print(leaders(arr))
