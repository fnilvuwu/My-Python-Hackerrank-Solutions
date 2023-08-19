_ = input()
n = list(map(int, input().split()))
print(all([i>=0 for i in n]) and any([str(j)[:len(str(j))//2]==str(j)[len(str(j))//2 + 1:] for j in n]))
