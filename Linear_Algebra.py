import numpy
n = int(input())
a = []
for i in range(n):
    a.append(input().split())

a = numpy.array(a, float)
print(round(numpy.linalg.det([a])[0], 2))
