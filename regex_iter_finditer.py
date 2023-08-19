import re
s = input()
m = re.findall(r'(?<=[^AIUEOaiueo])[AIUEOaiueo]{2,}(?=[^AIUEOaiueo])', s)
if m:
    for i in m:
        print(i)
else:
    print(-1)
