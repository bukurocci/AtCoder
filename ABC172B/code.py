def main():
  S = input()
  T = input()

  ans = 0

  for i, c in enumerate(S):
    if T[i] != c:
      ans += 1

  print(ans)

if __name__ == "__main__":
  main()