import numpy
numpy.set_printoptions(sign=' ')

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
  a.append(input().split())
for i in range(n):
  b.append(input().split())
  
a = numpy.array(a, int)
b = numpy.array(b, int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
