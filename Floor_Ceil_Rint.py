import numpy
my_array = numpy.array(input().split(), float)
numpy.set_printoptions(sign=" ")
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))
