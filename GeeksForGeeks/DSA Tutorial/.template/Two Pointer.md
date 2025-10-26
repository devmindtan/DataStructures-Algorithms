```python
def two_pointer(arr):
    l = 0
    r = len(arr) - 1   # hoặc r = 0

    while l < r:       # hoặc while r < len(arr)
        # Xử lý arr[l], arr[r]

        if < điều kiện nào đó > :
            l += 1
        elif < điều kiện khác > :
            r -= 1
        else:
            # có thể là hoán đổi, hoặc lưu kết quả