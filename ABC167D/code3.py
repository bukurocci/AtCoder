def main():
  N, K = list(map(int, input().split()))
  A = list(map(int, input().split()))

  d = 60
  to = [[0] * N for _ in range(d)]

  for i in range(N):
    #テレポート距離が2^0のデータを入れる
    #これは入力A1〜ANと同じ
    to[0][i] = A[i] - 1 #0-indexedにする

  for i in range(1, d):
    for j in range(N):
      to[i][j] = to[i-1][to[i-1][j]]

  v = 0
  for i in range(d-1, -1, -1):
    l = 1 << i

    if(K >= l):
      v = to[i][v]
      K -= l

  print(v + 1)

if __name__ == "__main__":
  main()