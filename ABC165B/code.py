import math

X = int(input())

p = 1.01
m = 100
y = 0

while m < X:
  m = math.floor(m * p)
  y += 1

print(y)