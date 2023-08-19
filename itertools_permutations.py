from itertools import permutations
s, k = input().split()
k = int(k)
for i in list(permutations(sorted(s), k)):
    print(*i, sep="")

