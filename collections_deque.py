# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())
for i in range(N):
    input_list = input().split()
    if len(input_list) > 1:
        command, input_value = input_list[0], input_list[1]
        if command == "append":
            d.append(input_value)
        elif command == "appendleft":
            d.appendleft(input_value)
    else:
        command = input_list[0]
        if command == "pop":
            d.pop()
        elif command == "popleft":
            d.popleft()

for i in d:
    print(i, end=" ")
