import math


def main():
  x1, y1, r = list(map(int, input().split()))
  x2, y2, x3, y3 = list(map(int, input().split()))

  # 左上
  d1 = math.sqrt((x2 - x1) ** 2 + (y3 - y1) ** 2)
  # 右上
  d2 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
  # 右下
  d3 = math.sqrt((x3 - x1) ** 2 + (y2 - y1) ** 2)
  # 左下
  d4 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

  # 赤の丸が青の矩形に対して完全に内側に存在するかどうか
  if x1 - r >= x2 and y1 - r >= y2 and x1 + r <= x3 and y1 + r <= y3:
    print("NO")
  else:
    print("YES")

  # 赤の丸が青の矩形を完全に含んでいるかどうか
  if d1 <= r and d2 <= r and d3 <= r and d4 <= r:
    print("NO")
  else:
    print("YES")

if __name__ == "__main__":
  main()