# import random
# import string

# import requests
# import json


# def generate_random_text(num_chars: int) -> str:
#     """Tạo ra một chuỗi ngẫu nhiên với đúng num_chars ký tự"""
#     # Ở đây mình sinh ngẫu nhiên từ bảng chữ cái + khoảng trắng
#     chars = string.ascii_letters + string.digits + " "
#     text = ''.join(random.choice(chars) for _ in range(num_chars))
#     return text


# # Ví dụ: tạo 100000 ký tự
# random_text = generate_random_text(10000000)

# # Kiểm tra độ dài
# print("Số ký tự:", len(random_text))


# # API_KEY = "YOUR_API_KEY"
# # MODEL = "gemini-1.5-flash"  # hoặc gemini-1.5-pro

# url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:countTokens?key=AIzaSyAFTB2zxZs23M9QNeyAJszpLy8_dcvPJE8"

# payload = {
#     "contents": [
#         {
#             "parts": [
#                 {"text": random_text}
#             ]
#         }
#     ]
# }

# response = requests.post(
#     url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

# print("Kết quả countTokens:", response.json())


# points = [(1, 2), (3, 1), (2, 5)]
# # Sắp theo hoành độ, rồi tung độ
# sorted_points = sorted(points, key=lambda x: (x[0], x[1]))
# print(sorted_points)

# import math
# # print(7.3 % 10)
# a = (1+3+math.sqrt(11)**1)

# # Nếu bạn muốn lấy 1 số sau dấu phẩy:
# result_1 = int((a - int(a)) * 10)  # Lấy 1 chữ số sau dấu phẩy

# # Nếu muốn lấy 2 số sau dấu phẩy:
# result_2 = int((a - int(a)) * 100)  # Lấy 2 chữ số sau dấu phẩy

# # print(result_1)  # 3
# # print(result_2)  # 34


# def solve():
#     t, m = map(int, input().split())
#     x = (1+3+math.sqrt(11))**t
#     print(int(x))
#     # res = int((x - int(x)) * m) % m
#     # print(x, res)


# solve()
# # print(3/10)
# # print(53/100)
# # print(solve())

# def solve():
#     low, high = 0, 16
#     for _ in range(4):
#         mid = (low + high) // 2
#         print("?", mid, flush=True)   # gửi câu hỏi đến judge
#         resp = input().strip()        # nhận phản hồi: "<", ">", "="

#         if resp == "=":
#             print("!", mid, flush=True)
#             return
#         elif resp == "<":
#             low = mid + 1
#         else:  # resp == ">"
#             high = mid - 1

#     # sau 4 lần hỏi, đoán nốt
#     print("!", low, flush=True)


# solve()


# import random


# def random_large_positive_integers(n):
#     """Sinh n số nguyên dương rất lớn (1 → 10^18)."""
#     return [random.randint(1, 10**5) for _ in range(n)]


# # Ví dụ:
# n = 1000000
# numbers = random_large_positive_integers(n)
# less_1e4 = sum(1 for x in numbers if x < 10000)
# print(f"Số nhỏ hơn {n:,}: {less_1e4:,} ({less_1e4 / len(numbers) * 100:.2f}%)")
# with open("output.txt", "w") as f:
#     f.write(" ".join(map(str, numbers)))
# print(" ".join(map(str, numbers)))
num = 215123123
# n = len(str(num))
# arr = [0] * n

# for i in range(n-1, -1, -1):
#     arr[i] = num % 10
#     num //= 10

# str_num = str(num)
# arr = [int(num) if int(num) <= 2 else None for num in str_num]


print(1 % 2)
