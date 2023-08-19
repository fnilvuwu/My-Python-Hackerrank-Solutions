from collections import defaultdict

# Read the group sizes
n, m = map(int, input().split())

# Create a defaultdict to store the occurrences of each element in group A
count_a = defaultdict(list)

# Read the elements of group A and store their positions
for i in range(n):
    element = input()
    count_a[element].append(i + 1)

# Create a defaultdict to store the occurrences of each element in group B
myList = []

# Read the elements of group B and store their positions
for i in range(m):
    element = input()
    myList.append(element)


# Print the positions of each element in group B
for element in myList:
    if element in count_a:
        print(" ".join( map(str,count_a[element])))
    else:
        print(-1)
