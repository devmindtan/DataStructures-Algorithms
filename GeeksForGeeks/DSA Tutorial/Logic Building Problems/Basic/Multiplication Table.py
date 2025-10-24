def getTable(n):
    ans = [0] * 10
    for i in range(0, 10):
        ans[i] = n * (i+1)
    return ans


print(getTable(68), end=" ")
