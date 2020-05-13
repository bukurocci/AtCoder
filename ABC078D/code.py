def main():
  N, M = list(map(int, input().split()))

  pass_count = N - M

  a = 100 * pass_count + 1900 * M
  r = 1 - (0.5 ** M)

  print(int(a / (1 - r)))


if __name__ == "__main__":
  main()