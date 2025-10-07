import random
import string

import requests
import json


def generate_random_text(num_chars: int) -> str:
    """Tạo ra một chuỗi ngẫu nhiên với đúng num_chars ký tự"""
    # Ở đây mình sinh ngẫu nhiên từ bảng chữ cái + khoảng trắng
    chars = string.ascii_letters + string.digits + " "
    text = ''.join(random.choice(chars) for _ in range(num_chars))
    return text


# Ví dụ: tạo 100000 ký tự
random_text = generate_random_text(10000000)

# Kiểm tra độ dài
print("Số ký tự:", len(random_text))


# API_KEY = "YOUR_API_KEY"
# MODEL = "gemini-1.5-flash"  # hoặc gemini-1.5-pro

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:countTokens?key=AIzaSyAFTB2zxZs23M9QNeyAJszpLy8_dcvPJE8"

payload = {
    "contents": [
        {
            "parts": [
                {"text": random_text}
            ]
        }
    ]
}

response = requests.post(
    url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

print("Kết quả countTokens:", response.json())
