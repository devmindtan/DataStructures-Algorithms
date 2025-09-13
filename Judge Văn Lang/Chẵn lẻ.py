# C1:
def chan_le(n):
    if (n % 2 == 0 and n > 0):
        return "Yes"
    else:
        return "No"


for i in range(int(input())):
    print(chan_le(int(input())))

# C2:
for i in range(int(input())):
    print("No" if int(input()) & 1 else "YES")
