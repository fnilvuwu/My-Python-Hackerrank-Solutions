# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mySet1 = set()
[mySet1.add(x) for x in input().split()]
    
m = int(input())
mySet2 = set()
[mySet2.add(x) for x in input().split()]
    
unionSet = mySet1.union(mySet2)
print(len(unionSet))
