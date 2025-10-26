# h=(d+[13(m+1)/5​]+y+[y/4​]−[y/100]+[y/400]) % 7
def getDayOfWeek(d, m, y):
    if m < 3:
        m += 12
        y -= 1

    m1 = d+(13*(m+1)//5)
    m2 = y + (y//4) - (y//100) + (y//400)

    h = (m1 + m2) % 7
    hash_table = {2: "Monday", 3: "Tuesday", 4: "Wednesday",
                  5: "Thursday", 6: "Friday", 0: "Saturday", 1: "Sunday"}
    return hash_table.get(h), h


d = 4
m = 12
y = 38
print(getDayOfWeek(d, m, y))
