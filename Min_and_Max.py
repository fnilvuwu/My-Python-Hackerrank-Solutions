import numpy

n, _ = map(int, input().split())
my_array = numpy.array([input().split() for i in range(n)], int)

print(numpy.max(numpy.min(my_array, axis = 1)))
