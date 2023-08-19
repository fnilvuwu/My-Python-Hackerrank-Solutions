import re
s = []
for i in range(int(input())):
    s.append(input())

s = "\n".join(s)
while " && " in s or " || " in s:
  s = re.sub(r"\s&&\s|\s&&$|^&&\s", " and ", s)
  s = re.sub(r"\s\|\|\s|\s\|\|$|^\|\|\s", " or ", s)
  
print(s)
