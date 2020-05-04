import math

def F(a, b):
  return len(str(a)) if a > b else len(str(b))

def main():
  N = int(input())
  ans = len(str(N))
  n_sq = math.floor(math.sqrt(N))

  for i in range(n_sq, 0, -1):
    if(N % i == 0):
      j = N // i
      ans = F(i, j)
      break

  print(ans)

if __name__ == "__main__":
    main()