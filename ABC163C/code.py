N = int(input())
A = list(map(int, input().split()))

S = [0] * N

for i in range(N - 1):
  S[A[i] - 1] += 1


for count in S:
  print(count)