n = int(input())
memo = [0] * 100
count = 0

for _ in range(n):
  d = int(input())

  if(memo[d-1] == 0):
    memo[d-1] = d


for d in memo:
  if(d > 0):
    count += 1

print(count)