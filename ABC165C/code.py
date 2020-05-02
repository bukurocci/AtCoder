N,M,Q = list(map(int, input().split()))
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
res = 0

def dfs(array):
  if(len(array) == N+1):
    global res
    p = 0

    for i in range(Q):
      # Abi - Aai = Ci を満たすようなi についてのdiの総和
      if(array[b[i]] - array[a[i]] == c[i]):
        p += d[i]
  
    res = max(p, res);

    return

  array.append(array[-1])
  while(array[-1] <= M):
    dfs(array[::])
    array[-1] += 1

for i in range(Q):
  a[i], b[i], c[i], d[i] = list(map(int, input().split()))

dfs([1])

print(res)


