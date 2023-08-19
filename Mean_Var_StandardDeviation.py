import numpy
n, _ = map(int, input().split())
myArray = []
for i in range(n):
    myArray.append(input().split())
    
my_array = numpy.array(myArray, int)
std_dev = numpy.std(my_array, axis = None)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print("{:.11f}".format(std_dev) if std_dev > 10**-11 else std_dev)
