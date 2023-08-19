k = int(input())
myList = list(map(int, input().split()))

count_dict = {}
for num in myList:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num in myList:
    if count_dict[num] == 1:
        print(num)
