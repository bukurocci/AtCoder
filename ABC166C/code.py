# N が展望台の数
# M が展望台を結ぶ道の数
N, M = list(map(int, input().split()))

# 展望台の標高
H = list(map(int, input().split()))

# 各展望台ごと周辺で一番大きな展望台の高さ
highest = [True] * N

res = 0

for i in range(M):
  a, b = list(map(int, input().split()))

  a = a - 1
  b = b - 1

  if(highest[a]):
    highest[a] = H[a] > H[b]
    
  if(highest[b]):
    highest[b] = H[a] < H[b]

for i, value in enumerate(highest):
  if(highest[i]):
    res += 1

print(res)