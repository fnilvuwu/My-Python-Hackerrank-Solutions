from collections import namedtuple

n = int(input())

Student = namedtuple('Student', ' '.join(input().split()))

print(sum([int(Student(*input().split()).MARKS) for i in range(n)]) /
      n)
