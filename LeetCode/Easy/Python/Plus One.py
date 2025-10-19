from typing import List


def plusOne(digits: List[int]) -> List[int]:
    arr = list(map(str, digits))
    merge = "".join(arr)
    plus_one = int(merge) + 1
    res = []
    for num in str(plus_one):
        res.append(int(num))

    return res


digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [9]
print(plusOne(digits))
