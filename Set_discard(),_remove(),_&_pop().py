_ = int(input())
s = set(map(int, input().split()))
n = int(input())

for i in range(n):
    user_input = input().split()
    if (len(user_input) > 1):
        opr, num = user_input
        getattr(s, opr)(int(num))
    else:
        opr = user_input[0]
        getattr(s, opr)()

print(sum(s))
