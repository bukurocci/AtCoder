
def main():
  # N: スイッチの数
  # M: 電球の数
  N,M = list(map(int, input().split()))

  ans = 0

  # 電球i番目と関連するスイッチ番号を対応させるための配列を作る
  s = [[] for i in range(M)]

  # 電球とスイッチの対応を行う処理
  for i in range(M):
    row = list(map(int, input().split()))
    k = row[0]

    for j in range(1, k+1):
      # i 番目の電球にツナっがっている、スイッチ番号を配列に突っ込んでいく
      s[i].append(row[j] - 1)

  # 電球が光る条件
  # 電球に対応するスイッチがON担っている数を2で割ってあまりがpiと同じなら電球はついている
  p = list(map(int, input().split()))

  # スイッチのON/OFFパターン全探索
  for i in range(1 << N):
    ok = True

    # j番目電球について考える
    for j in range(M):
      count = 0

      #j番目の電球に繋がっているスイッチがついているかどうかを確認する
      for value in s[j]:
        # スイッチ番号分右にビットシフトして1と&をとると、該当のスイッチ番号のスイッチがONになっているかわかる
        # Nが96の場合を考えるとスイッチとの関係は以下になる
        # 96 = 0b0001100000 = 0-indexedで5番目と6番目のスイッチがONになっていると取れる
        # 0b0001100000 >> 5 で 0b00011 なり、 1と & をとると 0b00001となる
        # これを条件式で利用すると、スイッチ番号ごとのon/offがわかる
        if(i >> value & 1):
          count += 1

      #点灯条件と照らし合わせる
      if(count % 2 != p[j]):
        ok = False

    # 全部ついていたら条件を満たしたパターンとしてカウントアップする
    if(ok):
      ans += 1

  print(ans)

if __name__ == "__main__":
    main()