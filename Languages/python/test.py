# def solve():
#     t = int(input())
#     res = []
#     for i in range(t):
#         n = input()
#         for i in range(65, 91):
#             print(chr(i), end=" ")

#     return res


def solve():
    n = int(input())
    if n == 1:
        for i in range(65, 91):
            print(chr(i), end=" ")
    elif n == 2:
        for i in range(97, 123):
            print(chr(i), end=" ")


def main():
    # for n in solve():
    #     solve()
    solve()


main()
