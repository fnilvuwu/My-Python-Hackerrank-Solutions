from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
myList = [int(x) for x in input().split()]
myCounter = Counter(myList)
money = 0

n = int(input())
for i in range(n):
    key, price = [int(x) for x in input().split()]
    if myCounter[key] != 0:
        myCounter[key] = myCounter[key] - 1
        money += price

print(money)
