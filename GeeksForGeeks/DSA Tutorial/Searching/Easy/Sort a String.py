MAX_CHAR = 26


def sort(s):
    char_count = [0] * MAX_CHAR

    for ch in s:
        char_count[ord(ch) - ord('a')] += 1

    result = ''
    for i in range(MAX_CHAR):
        for _ in range(char_count[i]):
            result += chr(i + ord('a'))

    return result


s = "edcabb"
print(sort(s))
