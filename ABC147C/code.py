
def main():
  N = int(input())

  ## 証言を入れる
  p = [[] for _ in range(N)]

  ans = 0

  for i in range(N):
    A = int(input())

    for j in range(A):
      p[i].append(list(map(int, input().split())))

  for i in range(1 << N):
    d = [0] * N

    for j in range(N):
      # 0-indexedで考える
      # 下i桁目を0桁目に持ってきて1と&をとると、i番目の人が正直者のフラグが立っているかどうかが判定できる
      if(i >> j & 1):
        d[j] = 1

    ok = True
    
    for j, _ in enumerate(p):
      #j人目の証言について確認する
      #j人目に正直者フラグが立っていた時だけ確認すれば良い
      if(d[j]):

        for k, _ in enumerate(p[j]):
          x, y = p[j][k]
          x -= 1
          if(d[x] != y):
            ok = False

    if(ok):
      # あり得る人数を知りたいので条件をパスしたものでbitの1が立っている箇所を調べる
      ans = max(ans, bin(i).count("1"))

  print(ans)

if __name__ == "__main__":
    main()