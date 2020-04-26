A,B = list(map(int, input().split()))

res = -1

for i in range(1, (B + 1) * 10):
  x = int(i * 0.08)
  y = int(i * 0.1)

  if(A == x and B == y):
    res = i
    break

print(res)