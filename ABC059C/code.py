def main():
  N = int(input())
  a = list(map(int, input().split()))

  avg = round(sum(a) / len(a))

  m = 201
  n = 0

  ans = 0

  for value in a:
    diff = value - avg

    if(diff < m):
      m = diff
      n = value - diff

  for value in a:
    ans += (n - value) ** 2

  print(ans)


if __name__ == "__main__":
  main()