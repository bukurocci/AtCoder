def main():
  A,B,C = list(map(int, input().split()))

  ans = "NO"

  for i in range(1, B+1):
    if((A * i) % B == C):
      ans = "YES"
      break

  print(ans)

if __name__ == "__main__":
  main()