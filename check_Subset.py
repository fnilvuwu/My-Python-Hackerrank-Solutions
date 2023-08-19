t = int(input())

output = []
for i in range(t):
    a_len = int(input())
    a = [int(x) for x in input().split()]
    set_a = set(a)
    b_len = int(input())
    b = [int(x) for x in input().split()]
    set_b = set(b)
    if set_a.issubset(set_b):
        output.append(True)
    else:
        output.append(False)

for i in output:
    print(i)
