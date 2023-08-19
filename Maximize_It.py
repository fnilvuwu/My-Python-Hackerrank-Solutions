import itertools

k, m = map(int, input().split())
myList = []

for _ in range(k):
    myList.append(list(map(int, input().split()[1:])))

max_modulo = 0

for combination in itertools.product(*myList):
    modulo = sum([x**2 for x in combination]) % m
    max_modulo = max(max_modulo, modulo)

print(max_modulo)
