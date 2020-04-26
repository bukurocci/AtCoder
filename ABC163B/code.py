N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

cost = 0;
for i in range(M):
  cost += A[i]

print(N - cost if cost <= N else -1)
