def firstOccurence(txt, pat):
    for i in range(len(txt)):
        if (txt[i:i+len(pat)] == pat):
            return i
    return -1


txt = "GeeksForGeeks"
pat = "Fr"

txt = "GeeksForGeeks"
pat = "For"

txt = "vpxowgsdgirfyaevnijubuuqevlrpeysxjfmesyjeg"
pat = "jfmesyjeg"
# print(len(txt))
# print(txt[33:33+len(pat)])
print(firstOccurence(txt, pat))
