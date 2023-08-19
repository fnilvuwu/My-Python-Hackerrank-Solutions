import numpy

n, _ = map(int, input().split())
my_array = []
for i in range(n):
    my_array.append([int(x) for x in input().split()])

my_array = numpy.array(my_array)
print(numpy.transpose(my_array))
print(my_array.flatten())
