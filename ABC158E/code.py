N, P = list(map(int, input().split()))
S = input()

#累積和を求めるため後ろから処理したい。配列は逆転しておく。
revS = S[::-1] 


# 10が素数であまり0、つまり2か5の場合
# 区間の下1けた目の数によって、どれだけ左側に伸ばして行っても
# 必ず割り切れる
if(10 % P == 0):
  res = 0

  for index, num in enumerate(revS):
    if(int(num) % P == 0) :
      res += len(revS) - index

  print(res)

else:

  #累積和を入れておく
  cs = 0

  ## あまりの値のカウント
  counts = [0] * P

  ## 累積和の初項は0になる
  ## 余りの値をindexにして配列 counts に同じ余りの値の個数を記録するので
  ## 初項の分は先に処理しておく
  counts[cs] += 1

  ## 桁
  d = 1

  ## 2項目からはfor文を使って同じ余りの値のカウントを行う処理する
  for num in revS:
    m = (int(num) * d) % P
    cs = (cs + m) % P

    counts[cs] += 1

    # 次の桁へ移動
    d *= 10

    # 桁が巨大になりすぎるのであまりを撮っておく
    # 掛け算の最中にあまりを撮るのは問題ない
    d %= P

  res = 0

  for n in counts:
    # 同じ余りの値がn個あったとして、重複なく2つ取り出す方法はnC2個
    res += n * (n - 1) // 2

  print(res)







