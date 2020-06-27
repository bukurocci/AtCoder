
def main():
  N = int(input())
  d = [1] * (N)
  ans = 0

  for i in range(2, N+1):
    f = i

    while True:
      d[f - 1] += 1
      f += i

      if(f > N):
        break

  for K in range(1, N+1):
    ans += K * d[K-1]

  print(ans)

if __name__ == "__main__":
  main()