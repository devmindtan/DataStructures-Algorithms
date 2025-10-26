```python
def sliding_window(arr):
    l = 0
    for r in range(len(arr)):
        # Thêm phần tử arr[r] vào cửa sổ

        while <cửa sổ vi phạm điều kiện>:
            # Loại arr[l] ra khỏi cửa sổ
            l += 1

        # Ở đây cửa sổ [l..r] hợp lệ, xử lý hoặc cập nhật kết quả