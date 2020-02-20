N,Y = list(map(int, input().split()))

x = -1 #10000円札
y = -1 #5000円札
z = -1 #1000円札

for i in range(N+1):
  for j in range(N + 1 - i):
    k = (N - i - j)
    total = 10000 * i + 5000 * j + 1000 * k

    if(total == Y ):
      x,y,z = i,j,k

print("{} {} {}".format(x, y, z))