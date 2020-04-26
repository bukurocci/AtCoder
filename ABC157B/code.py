bingo = list(map(int, input().split()))
bingo.extend(list(map(int, input().split())))
bingo.extend(list(map(int, input().split())))

N = int(input())

res = "No"

for _ in range(N):
  num = int(input())

  for (index, value) in enumerate(bingo):
    if value == num:
      bingo[index] = 0


## 斜め判定
if bingo[0] == bingo[4] == bingo[8] == 0 or bingo[2] == bingo[4] == bingo[6] == 0:
  res = "Yes"

else:
  ## 縦判定
  for i in range(3):
    if (bingo[i] == bingo[i+3] == bingo[i+6] == 0 or bingo[3 * i] == bingo[3 * i + 1] == bingo[3 * i + 2] == 0):
      res = "Yes"
      break
  
print(res)