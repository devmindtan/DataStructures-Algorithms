def lengthOfLastWord(s: str) -> int:
    validate = s.split()
    last_word = validate[-1]
    count = 0
    for _ in last_word:
        count += 1
    return count


a = " sdfhs sdfjsfk   sd sdf "
print(lengthOfLastWord(a))
# print(" ".join(a.split()))
