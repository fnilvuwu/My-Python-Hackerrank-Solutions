cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    #Initial variable for the base case. 
    fibonnaciList = [0,1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    first = 0
    second = 1
    n -= 2
    while n > 0:
        fibonnaciList.append(first+second)
        temp = second
        second += first
        first = temp
        n -= 1
    return fibonnaciList
