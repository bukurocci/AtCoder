N, K = list(map(int, input().split()))

nusuke = [0] * N
res = 0

for i in range(K):
  d = int(input())
  a = list(map(int, input().split()))
  for j in range(d):
    nusuke[a[j] - 1] += 1

for value in nusuke:
  if(value == 0):
    res += 1

print(res)