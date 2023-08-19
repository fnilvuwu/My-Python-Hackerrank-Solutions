# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))

print(*sorted(a.union(b).difference(a.intersection(b))), sep="\n")
