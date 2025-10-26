from math import gcd


def addFraction(num1, den1, num2, den2):
    if (den1 == den2):
        return (f"{num1+num2}/{den1}")
    else:
        # boi_so_chung = (lcm(den1, den2))
        boi_so_chung = den1 * den2
        num1 = num1 * den2
        num2 = num2 * den1
        uoc_so_chung = gcd((num1+num2), boi_so_chung)
        rut_gon_tu = int((num1 + num2)/uoc_so_chung)
        rut_gon_mau = int((boi_so_chung/uoc_so_chung))

        return (f"{rut_gon_tu}/{rut_gon_mau}")


num1 = 384
den1 = 887
num2 = 778
den2 = 916

# num1 = 1
# den1 = 5
# num2 = 1
# den2 = 6
print(addFraction(num1, den1, num2, den2))

# print(gcd(520915, 406246))
