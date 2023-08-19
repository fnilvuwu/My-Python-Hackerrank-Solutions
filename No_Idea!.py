# Read input from STDIN
n, m = map(int, input().split())
myArray = list(map(int, input().split()))

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

# Compute happy count
happiness = 0
for num in myArray:
    if num in set_A:
        happiness += 1
    elif num in set_B:
        happiness -= 1

# Print the final happiness
print(happiness)
