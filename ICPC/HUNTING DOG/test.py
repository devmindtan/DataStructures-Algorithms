import re
s = ".i.like.this.program.very.much."
# s = "v.f..gfc"
arr = re.split(r'\.+', s.strip("."))
val = ".".join(arr[::-1])
print(val)
