def distance(x1, y1, x2, y2):
    a = abs(x1-x2)
    b = abs(y1-y2)
    c = (a*a+b*b)**0.5
    floor = int(c)
    res = abs(floor - c)

    if (res > 0.5):
        floor += 1
    else:
        floor
    return floor


print(distance(0, 0, -2, 2))
print(distance(-20, 23, -15, 68))
