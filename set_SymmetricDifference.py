# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mySet1 = set()
[mySet1.add(x) for x in input().split()]
    
m = int(input())
mySet2 = set()
[mySet2.add(x) for x in input().split()]
    
sym_diffSet = mySet1.symmetric_difference(mySet2)
print(len(sym_diffSet))
