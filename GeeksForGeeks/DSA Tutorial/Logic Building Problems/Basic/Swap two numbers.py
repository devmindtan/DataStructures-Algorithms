def get(a: int, b: int):
    tmp = a
    a = b
    b = tmp
    return a, b


print(get(13, 9))
