def main():
  K = int(input())
  S = input()

  ans = S

  if(len(S) > K):
    ans = S[0:K] + "..."

  print(ans)

if __name__ == "__main__":
  main()