#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

A = list(zip(*matrix))
A = ''.join(''.join(i) for i in A)

# took the middle part
y = re.findall("[a-zA-Z0-9].+[a-zA-Z0-9]", A)
y = ''.join(y)
# took the first part
x = A.index(y)
x = A[:x]
# took the last part
z = re.findall(".+[a-zA-Z0-9]", A)
z = ''.join(z)
z = A[len(z):]

# remove any other element to single space
y = re.sub("[^a-zA-Z0-9]+", ' ', y)

print(x+y+z)
