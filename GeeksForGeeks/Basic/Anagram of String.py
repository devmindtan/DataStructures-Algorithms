# Anagram nghĩa là: 2 chuỗi có cùng tập hợp ký tự và số lần xuất hiện của ký tự (chỉ khác thứ tự thôi)

# C1
def remAnagram_c1(s1, s2):
    hash_table_1 = {}
    hash_table_2 = {}
    for ch in s1:
        hash_table_1[ch] = hash_table_1.get(ch, 0) + 1
    for ch in s2:
        hash_table_2[ch] = hash_table_2.get(ch, 0) + 1
    # print(hash_table_1)
    # print(hash_table_2)

    for ch in s2:
        if (ch in hash_table_1 and hash_table_1[ch] > 0):
            hash_table_1[ch] -= 1
            hash_table_2[ch] -= 1
    # print("--------------")
    # print(hash_table_1)
    # print(hash_table_2)
    sum_1 = sum(hash_table_1.values())
    sum_2 = sum(hash_table_2.values())
    return (sum_1 + sum_2)


# C2
def remAnagram_c2(s1, s2):
    hash_table = {}

    for ch in s1:
        hash_table[ch] = hash_table.get(ch, 0) + 1

    for ch in s2:
        hash_table[ch] = hash_table.get(ch, 0) - 1

    print(hash_table)

    return sum(abs(v) for v in hash_table.values())


# s1 = "bcadeh"
# s2 = "hea"

# s1 = "cddgk"
# s2 = "gcd"
s1 = "basgadhbfgvhads"
s2 = "sjdhgvbjdsbhvbvd"

# print(len(s1))
# print(len(s2))

print(remAnagram_c1(s1, s2))
print(remAnagram_c2(s1, s2))
