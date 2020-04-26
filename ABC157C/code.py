N, M = list(map(int, input().split()))

d = [-1] * N
illegal = False

for _ in range(M):
  s,c = list(map(int, input().split()))
  ## 代入できる条件
  ## 未代入または、前に代入された値と同じ
  if(d[s-1] == -1 or d[s-1] == c or d[s-1] == 0):
    d[s-1] = c
  else:
    illegal = True

if(len(d) > 1 and d[0] == 0):
  illegal = True

if(illegal):
  print(-1)
else:
  if(len(d) > 1 and d[0] == -1):
    d[0] = 1
  
  res = ""

  for value in d:
    if(value == -1):
      res += "0"
    else:
      res += str(value)

  print(res)