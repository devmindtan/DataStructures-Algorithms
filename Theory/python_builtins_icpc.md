
# 🐍 Tổng hợp hàm Built-in Python quan trọng cho ICPC

Việc sử dụng các **hàm built-in** và **thư viện chuẩn** giúp tiết kiệm thời gian, giảm bug và tối ưu hiệu năng trong các kỳ thi như **ICPC**.

---

## 🔹 I. Các hàm built-in quan trọng trong Python

### 📘 1. Hàm cơ bản thao tác với kiểu dữ liệu

| Hàm | Mô tả |
|------|-------|
| `len(x)` | Trả về độ dài (số phần tử) của chuỗi, list, tuple, dict... |
| `type(x)` | Kiểm tra kiểu dữ liệu của biến |
| `id(x)` | Trả về địa chỉ (id) của đối tượng |
| `isinstance(x, type)` | Kiểm tra biến có thuộc kiểu nào đó không |
| `hash(x)` | Lấy giá trị hash (dùng trong dict, set) |
| `repr(x)` | Chuỗi biểu diễn đối tượng (debug tiện) |
| `str(x)`, `int(x)`, `float(x)`, `bool(x)` | Ép kiểu dữ liệu |

---

### 🧮 2. Hàm toán học nhanh

| Hàm | Mô tả |
|------|-------|
| `abs(x)` | Giá trị tuyệt đối |
| `pow(a, b[, mod])` | Lũy thừa (có thể mod) |
| `round(x, n)` | Làm tròn đến n chữ số thập phân |
| `min(iterable)` / `max(iterable)` | Giá trị nhỏ nhất / lớn nhất |
| `sum(iterable, start=0)` | Tính tổng |
| `divmod(a, b)` | Trả về `(a // b, a % b)` |
| `all(iterable)` / `any(iterable)` | Kiểm tra toàn bộ True hoặc có ít nhất 1 True |
| `sorted(iterable, key=..., reverse=...)` | Sắp xếp nhanh |
| `enumerate(iterable, start=0)` | Duyệt list có cả chỉ số |
| `zip(a, b, ...)` | Gộp nhiều list lại theo vị trí |

---

### 📊 3. Làm việc với iterable / collections

| Hàm | Mô tả |
|------|-------|
| `map(func, iterable)` | Áp dụng hàm lên từng phần tử |
| `filter(func, iterable)` | Lọc các phần tử thỏa điều kiện |
| `reversed(iterable)` | Đảo ngược thứ tự |
| `range(start, stop, step)` | Sinh dãy số |
| `set()`, `list()`, `tuple()`, `dict()` | Tạo kiểu dữ liệu tương ứng |
| `next(iterator, default)` | Lấy phần tử tiếp theo trong iterator |

---

### 📂 4. Xử lý input/output

| Hàm | Mô tả |
|------|-------|
| `input()` | Đọc dòng input |
| `print()` | In ra màn hình |
| `open(file, mode)` | Mở file |
| `format()` / f-string | Định dạng chuỗi |

---

### 🧠 5. Hàm logic & lập trình

| Hàm | Mô tả |
|------|-------|
| `eval(expr)` | Thực thi chuỗi như code Python *(cẩn trọng)* |
| `exec(code)` | Thực thi code Python |
| `bin(x)`, `oct(x)`, `hex(x)` | Đổi hệ nhị / bát / thập lục phân |
| `ord(ch)` / `chr(num)` | Ký tự ↔ mã ASCII |
| `dir(obj)` | Liệt kê thuộc tính, phương thức |

---

### 🧰 6. Thư viện chuẩn cực hữu ích trong ICPC

| Thư viện / Hàm | Tác dụng |
|-----------------|----------|
| `itertools.permutations()` | Sinh hoán vị |
| `itertools.combinations()` | Sinh tổ hợp |
| `itertools.product()` | Tích Descartes |
| `math.gcd(a, b)` / `math.lcm(a, b)` | Ước chung lớn nhất / bội chung nhỏ nhất |
| `math.isqrt(x)` | Căn nguyên chính xác |
| `bisect.bisect_left()` / `bisect_right()` | Tìm vị trí chèn nhị phân |
| `heapq.heappush()` / `heapq.heappop()` | Priority queue |
| `collections.Counter()` | Đếm tần suất |
| `collections.deque()` | Hàng đợi hai đầu |
| `collections.defaultdict()` | Dict có giá trị mặc định |
| `functools.lru_cache()` | Cache đệ quy / DP |

---

### ⚡ 7. Hàm đặc biệt dùng trong thi thuật toán

| Hàm | Mô tả |
|------|-------|
| `max(arr, key=...)` | Chọn phần tử lớn nhất theo key |
| `min(arr, key=...)` | Chọn phần tử nhỏ nhất theo key |
| `sum(1 for x in arr if x % 2 == 0)` | Đếm phần tử thỏa điều kiện |
| `sorted(set(arr))` | Sắp xếp và loại trùng |
| `list(map(int, input().split()))` | Đọc mảng số nguyên |
| `*map(int, input().split())` | Unpack trực tiếp các giá trị |

---

## 🔹 II. Mẹo thi ICPC nhanh hơn

1. **Dùng input nhanh:**
   ```python
   import sys
   input = sys.stdin.readline
   ```

2. **In kết quả nhanh:**
   ```python
   res = []
   for _ in range(t):
       res.append(str(answer))
   print("\n".join(res))
   ```

3. **Tránh dùng `pop(0)`** → dùng `deque`.

4. **Dùng `bisect`, `heapq`, `lru_cache` để tối ưu.**

---

**Tổng kết:** Nắm vững các hàm built-in giúp bạn code nhanh, chính xác và hiệu quả hơn trong các bài toán lập trình ICPC.
