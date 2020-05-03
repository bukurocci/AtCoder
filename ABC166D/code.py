import math

X = int(input())
M = 500

def culc():
  for a in range(-M, M):
    a5 = pow(a, 5)

    for b in range(-M, M):
      b5 = pow(b, 5)

      if(a5 - b5 == X):
        print(" ".join(map(str, [a, b])))
        return

culc()