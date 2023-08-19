# Enter your code here. Read input from STDIN. Print output to STDOUT
height, width = [int(x) for x in input().split()]
c= ".|."
welcome ="WELCOME"

for i in range(1, height, 2):
    print((c*i).center(width, '-'))

print(welcome.center(width, '-'))

for i in range(height-2, 0, -2):
    print((c*i).center(width, '-'))
