a,b,c = list(map(int, input().split()))
res = "No"

if(not a == b == c and (a == b or b == c or a == c)):
  res = "Yes"

print(res)

