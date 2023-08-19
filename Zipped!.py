# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = input().split()

score_list = []
for i in range(int(X)):
    score_list.append([float(j) for j in list(input().split())])

zipped_list = list(zip(*score_list))

for i in zipped_list:
    print(sum(i)/len(i))


