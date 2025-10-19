def strStr(haystack: str, needle: str) -> int:
    i = 0
    j = len(needle)
    while j <= len(haystack):
        if (haystack[i:j] == needle):
            return i
        i += 1
        j += 1

    return -1


haystack = "sadbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"
haystack = "mississippi"
needle = "issip"
# haystack = "a"
# needle = "a"
print(strStr(haystack, needle))
# print(needle[0:3])
