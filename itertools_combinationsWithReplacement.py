from itertools import combinations_with_replacement
# Enter your code here. Read input from STDIN. Print output to STDOUT
string, n = input().split()
n = int(n)

tupleList = list(combinations_with_replacement(sorted(string), n))

for item in tupleList:
    print(*item, sep="")
