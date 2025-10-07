# C1 (O(n*2))
def binarySubstring_c1(s):
    check = 0
    for i in range(len(s)):
        if (s[i] == "1"):
            for j in range(len(s) - 1, i, -1):
                if (s[j] == "1"):
                    check += 1
    return check


# C2 - (O(n*2))
def binarySubstring_c2(s):
    check = 0
    for i in range(len(s)):
        if (s[i] == "1"):
            for j in range(i+1, len(s)):
                if (s[j] == "1"):
                    check += 1
    return check


# C3 - (O(n))
def binarySubstring_c3(s):
    ones = s.count("1")   # Đếm số '1'
    return ones * (ones - 1) // 2


# C4 - (O(n))
def binarySubstring_c4(s):
    count = 0
    res = 0
    for ch in s:
        if (ch == "1"):
            res += count
            count += 1
    return res


# s = "00011110"
s = "1111"
# s = "01101"

# binarySubstring(s)

print(binarySubstring_c4(s))
