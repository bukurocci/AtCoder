N = int(input())
res = "Yes"

for _ in range(N):
  t,x,y = list(map(int, input().split()))

  if(t < x + y): #この場合は旅程を立てられない
    res = "No"
    break

  is_even = (x + y) % 2 == 0

  if(t % 2 == 0): # tが偶数の場合x+yも偶数
    if(not is_even):
      res = "No"
      break
  else: # tが奇数の場合x+yも奇数
    if(is_even):
      res = "No"
      break
    

print(res)