
def main():
  N = int(input())

  ## 証言を入れる
  p = [[-1 for i in range(N)] for j in range(N)]

  ans = 0

  for i in range(N):
    A = int(input())

    for j in range(A):
      x, y = list(map(int, input().split()))
      x -= 1
      p[i][x] = y


  for i in range(1 << N):
    d = [0] * N

    for j in range(N):
      # 0-indexedで考える
      # 下i桁目を0桁目に持ってきて1と&をとると、i番目の人が正直者のフラグが立っているかどうかが判定できる
      if(i >> j & 1):
        d[j] = 1

    ok = True
    
    for j in range(N):
      if(d[j]):
        for k in range(N):
          if(p[j][k] == -1):
            continue
          if(p[j][k] != d[k]):
            ok = False

    if(ok):
      ans = max(ans, bin(i).count("1"))

  print(ans)

if __name__ == "__main__":
    main()