X, Y = list(map(int, input().split()))

ans = "No";

for i in range(0, X+1):
  a = i * 2
  b = (X - i) * 4

  if((a + b) == Y):
    ans = "Yes"
    break

print(ans);