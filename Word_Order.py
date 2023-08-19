# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
string_unique = {}
for i in range(n):
    new_input = input()
    if new_input in string_unique:
        string_unique[new_input] = string_unique[new_input] + 1
    else:
        string_unique[new_input] = 1

print(len(string_unique))

for key in string_unique:
    print(string_unique[key], end=' ')
