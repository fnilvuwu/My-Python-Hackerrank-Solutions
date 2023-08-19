# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a/b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
