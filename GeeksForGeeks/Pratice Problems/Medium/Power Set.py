from itertools import combinations


def AllPossibleStrings_c1(s):
    n = len(s)
    result = []
    # Tạo tổ hợp từ 1 ký tự trở lên
    for r in range(1, n+1):
        indices = list(range(r))  # lưu các chỉ số tạm thời
        while True:
            # ghép ký tự theo indices
            combo = "".join(s[i] for i in indices)
            result.append(combo)

            # tìm chỉ số nào tăng tiếp theo
            for i in reversed(range(r)):
                if indices[i] != i + n - r:  # chạy ngược lại để kiểm tra các tổ hợp đã đủ chưa
                    break
            else:
                # không còn chỉ số nào tăng → kết thúc
                break

            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
    result.sort()
    return result


def AllPossibleStrings_c2(s):
    res = []
    n = len(s)
    for r in range(1, n+1):
        for comb in combinations(s, r):
            res.append("".join(comb))
    res.sort()
    return res


def AllPossibleStrings_c3(s):
    result = []

    def backtrack(start, path):
        if len(path) >= 1:
            result.append("".join(path))
        for i in range(start, len(s)):
            path.append(s[i])          # chọn ký tự i
            backtrack(i+1, path)       # đệ quy phần còn lại
            path.pop()                 # bỏ ký tự i, thử ký tự tiếp theo

    backtrack(0, [])
    return result


s = "abcd"
print(AllPossibleStrings_c1(s))
print(AllPossibleStrings_c2(s))
print(AllPossibleStrings_c3(s))
