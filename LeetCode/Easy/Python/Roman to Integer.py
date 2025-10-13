def romanToInt(s: str):
    hash_table = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    res = 0
    j = 1
    i = 0
    if (len(s) == 1):
        return hash_table[s[i]]
    while j < len(s):
        if (hash_table[s[i]] >= hash_table[s[j]]):
            res += hash_table[s[i]]
        else:
            res -= hash_table[s[i]]
        if (j == len(s) - 1):
            res += hash_table[s[-1]]
            break
        j += 1
        i += 1
    return res


s = "II"
# s = "LVIII"
# s = "MCM"
# s = "MCMXCIV"
# s = "D"
print(romanToInt(s))
