def main():
  N, K = list(map(int, input().split()))
  A = list(map(int, input().split()))

  # 各indexに対応する町に訪れるために必要な距離をいれる
  o = [-1] * (N+1)

  # 訪問順に並べた町を入れえる
  s = []

  # 現在の町
  v = 1

  # 訪れたところに再訪するまで続ける
  while(o[v] == -1):
    #sの配列長をいれることで、A[0]からA[v-1]番目の街の距離がどのくらいかを保存する
    o[v] = len(s)
    s.append(v)
    v = A[v - 1] # Aは0-indexedだから v-1

  # ループを開始する街までの距離
  l = o[v]
  # 再訪が確認できたら、訪問順を収めた配列長（A[0]からループの終端までの距離）から、ループの開始地点の距離を引くと周期が求まる
  c = len(s) - l

  # 距離Kまでにループが始まっていなければ訪問順のK番目
  if(K < l):
    print(s[K])
  # ループが始まっていたら
  else:
    k = K - l
    k %= c
    print(s[l + k])


if __name__ == "__main__":
  main()