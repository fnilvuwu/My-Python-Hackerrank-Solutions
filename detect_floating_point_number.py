# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    try:
        s = input()
        print(True) if "." in str(s) and float(s) else print(False)
    except:
        print(False)
