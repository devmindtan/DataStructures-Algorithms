variables = [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]]
target = 2

variables = [[39, 3, 1000, 1000]]
target = 17

res = []
for i in range(len(variables)):
    sub = variables[i]
    for j in range(len(sub)):
        modul = (sub[0]**sub[1] % 10)**sub[2] % sub[3]
    if (modul == target):
        res.append(i)
print(res)
