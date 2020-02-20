N = int(input())
A = list(map(int, input().split()))

res = "APPROVED"

for i in range(N):
  # 偶数が3or5で割り切れるので、まずは偶数判定をする
  if(A[i] % 2 == 0):
    # 3でも5でも割り切れない = 余りが出たら、DENIED
    if(A[i] % 3 != 0 and A[i] % 5 != 0):
      res = "DENIED"
      break


print(res)
