def reverseWithSpacesIntact(s):
    s = list(s)
    l = 0
    r = len(s) - 1
    while l <= r:
        if (s[l] == " "):
            l += 1
        elif (s[r] == " "):
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return "".join(s)


s = "Help others"
s = "xg kn u ff vr j"
print(reverseWithSpacesIntact(s))
