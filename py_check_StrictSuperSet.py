a = set(map(int, input().split()))
n = int(input())
superset = True
for i in range(n):
    other_set = set(map(int, input().split()))
    if not a.issuperset(other_set) or other_set == a:
        superset = False
print(superset)
