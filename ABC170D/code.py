import math

def main():
  N = int(input())
  A = list(map(int, input().split()))
  A.sort()
  MAX = A[-1]
  dp = [True] * MAX
  c = [0] * MAX
  ans = 0

  for a in A:
    i = a - 1
    c[i] += 1

    if((not dp[i]) and c[i] > 1):
      continue

    e = a * 2    
    while e <= MAX:
      dp[e-1] = False
      e += a
      
  for v in A:
    i = v - 1
    if dp[i] and c[i] == 1:
      ans += 1

  print(ans)

if __name__ == "__main__":
  main()