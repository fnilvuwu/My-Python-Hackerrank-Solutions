input()
mySet = set([int(x) for x in input().split()])
for i in range(int(input())):
    command, _ = input().split()
    otherSet = [int(x) for x in input().split()]
    getattr(mySet, command)(otherSet)

print(sum(mySet))
