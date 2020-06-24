def main():
  N ,K = list(map(int, input().split()))
  P = list(map(int, input().split()))

  P.sort()

  print(sum(P[0:K]))


if __name__ == "__main__":
  main()