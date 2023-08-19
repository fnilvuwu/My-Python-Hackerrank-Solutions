import re
s = input() # Source String 
k = input() # String to be searched
pattern = re.compile(k)
r = pattern.search(s)
if not r: print(tuple([-1, -1]))
while r:
    print(tuple([r.start(), r.end() - 1]))
    r = pattern.search(s, r.start() + 1)
