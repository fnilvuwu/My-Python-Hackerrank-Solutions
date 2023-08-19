import re
s = [input() for i in range(int(input()))]
x = ["YES" if re.search(r"^[7-9]\d{9}$", i) else "NO" for i in s]
print(*x, sep="\n")
