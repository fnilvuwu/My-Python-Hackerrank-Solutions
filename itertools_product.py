from itertools import product
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(*list(product(a, b)))
