from math import factorial as f
from collections import Counter
# Practice Questions - Permutations and Combinations
# Question 1: How many ways can 5 books be arranged on a shelf?
n = 5
r = 5
ways = int(f(n)/f(n-r))
print(f"Q1: {ways} ways")

# Question 2: In how many ways can a committee of 3 be chosen from a group of 10 people?
n = 10
r = 3
ways = int(f(n)/(f(r)*f(n-r)))
print(f"Q2: {ways} ways")

# Question 3: How many 4-digit PIN codes can be created using the digits 0-9 if repetition is allowed?
# Mỗi vị trí có 10 cách, tổng 4 vị trí
n = 10
r = 4
ways = 10**4
print(f"Q3: {ways} ways")

# Question 4: A pizza shop offers 8 toppings. How many different 3-topping pizzas can be made?
n = 8
r = 3
ways = int(f(n)/(f(r)*f(n-r)))
print(f"Q4: {ways} ways")

# Question 5: In how many ways can 6 people be seated at a round table?
n = 6
r = 6
ways = int(f(n)/f(n-r))
print(f"Q5: {ways} ways")

# Question 6: How many ways are there to select 2 boys and 3 girls from a class of 5 boys and 6 girls?
n1, n2 = 5, 6
r1, r2 = 2, 3
boys = int(f(n1)/(f(r1)*f(n1-r1)))
girls = int(f(n2)/(f(r2)*f(n2-r2)))
ways = boys * girls
print(f"Q6: {ways} ways")

# Question 7: How many different 5-card hands can be dealt from a standard 52-card deck?
n = 52
r = 5
ways = int(f(n)/(f(r)*f(n-r)))
print(f"Q7: {ways} ways")


# Question 8: In how many ways can the letters of the word "MATHEMATICS" be arranged?
# Có chữ lặp nên phải tính giai thừa riêng cho từng chữ đó rồi nhân lại với nhau sau
word = "MATHEMATICS"
count = Counter(word)
res = 1
n = len(word)

for num in count.values():
    res *= f(num)

ways = int(f(n) / (res))
print(f"Q8: {ways} ways")


# Question 9: A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. How many ways are there to select 4 marbles?
n = 5 + 3 + 2
r = 4
ways = int(f(n)/(f(r)*f(n-r)))
print(f"Q9: {ways} ways")

# Question 10: How many ways are there to arrange the letters in the word "MISSISSIPPI"?
word = "MISSISSIPPI"
n = len(word)
count = Counter(word)
res = 1

for num in count.values():
    res *= f(num)
ways = int(f(n) / (res))
print(f"Q10: {ways} ways")
