from pympler import asizeof

s_list = ["a", "b", "c", "d"]
s_str = "abcd"

print(asizeof.asizeof(s_list))  # bao gồm cả các 'a','b','c'
print(asizeof.asizeof(s_str))
