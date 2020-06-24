def main():
  N = int(input())
  a = list(map(int, input().split()))

  rate = [3199, 2799, 2399, 1999, 1599, 1199, 799, 399, 1]

  c = [0] * len(rate)

  for v in a:
    for i, r in enumerate(rate):
      if(v > r):
        c[i] += 1
        break

  count = 0
  ans = [0,0]

  for v in c[1:]:
    if(v > 0):
      count += 1

  ans[0] = ans[1] = count

  if(c[0] > 0):
    if(count == 0):
      ans[0] = 1
      ans[1] = c[0]
    else:
      ans[1] += c[0]


  print(" ".join(map(str, ans)))


if __name__ == "__main__":
  main()