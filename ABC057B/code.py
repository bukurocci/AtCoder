def main():
  N, M = list(map(int, input().split()))

  p1 = []
  p2 = []

  for _ in range(N):
    x, y = list(map(int, input().split()))
    p1.append([x, y])
  
  for _ in range(M):
    c, d = list(map(int, input().split()))
    p2.append([c, d])

  for p in p1:
    x1, y1 = p
    near = 10 ** 9
    ans = 0
    
    for i, q in enumerate(p2):
      x2, y2 = q
      d = abs(x1 - x2) + abs(y1 - y2)

      if near > d:
        near = d
        ans = i
    
    print(ans + 1)

if __name__ == "__main__":
  main()