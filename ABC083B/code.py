n,a,b = list(map(int, input().split()))

total = 0

for i in range(n+1):
  x = sum(list(map(int, str(i))))
  
  if(a <= x <= b):
    total += i

print(total)