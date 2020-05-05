import math
N = int(input())
p = []
d = []

def dfs(route, visited, n):
  total = 0
  if(len(route) == n + 1):
    for i in range(1, N):
      x1, y1 = d[route[i]]
      x2, y2 = d[route[i+1]]
      total += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      
    return total

  route.append(0)

  for i in range(n):
    if(visited[i]):
      continue

    route[-1] = i
    v = visited[::]
    v[i] = True
    total += dfs(route[::], v, n)
  
  return total

for i in range(N):
  d.append(list(map(int, input().split())))

a = 1

for i in range(1, N+1):
  a *= i

print(dfs([-1], [False] * N, N) / a)

