import numpy

p = [float(x) for x in input().split()]
x = int(input())
print(numpy.polyval(p, x))
