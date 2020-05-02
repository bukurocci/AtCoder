K = int(input());
A,B = list(map(int, input().split()))

res = "NG"

if A % K == 0 or B % K == 0:
  res = "OK"
else:
  for i in range(A, B+1):
    if(i % K == 0):
      res = "OK"
      break

print(res)

