# def build_prefix(arr):
#     prefix = [0] * (len(arr) + 1)
#     for i in range(1, len(arr)+1):
#         prefix[i] = prefix[i-1] + arr[i-1]
#     return prefix

# arr = [2, 4, 6, 8]
# prefix = build_prefix(arr)

# # Ví dụ tính tổng từ index 1 đến 3 (4+6+8 = 18)
# l, r = 2, 3
# print(prefix[r+1] - prefix[l])  # 18


# import bisect


# a = [1, 3, 4, 6, 8, 10]
# x = 6
# pos = bisect.bisect_left(a, x)
# if pos < len(a) and a[pos] == x:
#     print("Found at index", pos)   # index = 3
# else:
#     print("Not found")

# arr = [(1, 5), (2, 3), (3, 7)]
# print(sorted(arr))                     # sắp theo phần tử đầu
# print(sorted(arr, key=lambda x: x[1])) # sắp theo phần tử thứ 2

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum += arr[i] - arr[i-k]
#     max_sum = max(max_sum, window_sum)

# print(max_sum)  # 9 (5+1+3)

# def reverse(n):
#     if n < 10:
#         return n
#     return n % 10 * 10**(len(str(n))-1) + reverse(n // 10)


# print(reverse(1234))  # 321
# print(reverse(45))   # 54
# print(reverse(907))  # 709

# x = "192.168.0.257"
# arr = [int(num) for num in x.split(".")]
# res = []
# for x in arr:
#     bits = [0] * 8
#     i = 7
#     while (x != 0 and i >= 0):
#         bits[i] = x % 2
#         x = x // 2
#         i -= 1
#     res.append("".join(str(b) for b in bits))


# output = ".".join(res)
# print(output)
from functools import reduce
nums = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
nums.remove(3)
s = reduce(lambda x, y: x + y, nums, 10)
print(product, s)
