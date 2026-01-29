def solve():
    t = int(input())
    res = []

    for _ in range(t):
        n = int(input())

        arr = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
        hang_tram = n // 100
        hang_chuc = (n // 10) % 10
        hang_don_vi = n % 10
        cach_doc = ""

        if hang_tram != 0:
            cach_doc = arr[hang_tram] + " tram "

        if hang_chuc > 0:
            if hang_chuc == 1:
                cach_doc += "muoi "
            else:
                cach_doc += arr[hang_chuc] + " muoi "
        else:
            if hang_tram > 0 and hang_don_vi > 0:
                cach_doc += "le "

        if hang_don_vi != 0:
            if hang_don_vi == 5 and hang_chuc > 0:
                cach_doc += "lam"
            else:
                cach_doc += arr[hang_don_vi]
        if hang_tram == 0 and hang_chuc == 0 and hang_don_vi == 0:
            cach_doc = "khong"
        res.append(cach_doc.strip())

    return res


def main():
    for n in solve():
        print(n)


main()
