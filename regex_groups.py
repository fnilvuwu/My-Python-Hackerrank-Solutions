import re
s = input()
m = re.search(r'(\w)(?!_)\1', s)
if m:
    print(m.group(1))
else:
    print(-1)
