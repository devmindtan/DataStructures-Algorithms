def isBalanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    print(pairs[']'])
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# Ý tưởng làm bài này
"""
1. Cho các cặp dấu cùng loại và ngược nhau vào trong hash_table
2. Kiểm tra theo kiểu stack (ngăn xếp - FILO (First in Last out))
    - Chỉ thêm dấu mở vào stack
    - So sánh dấu đóng có cùng loại với cái dấu mở không 
    - Nếu đúng thì bỏ dấu đó ra ngược lại thì sai vì khác loại
3. Và nếu stack rồng thì cũng sai vì luôn luôn phải mở trước khi đóng  
"""

print(isBalanced("[{()}]"))
# print(isBalanced("([]"))
# print(isBalanced("[(])"))
# print(isBalanced("[()()]{}"))
# print(isBalanced("}]"))
