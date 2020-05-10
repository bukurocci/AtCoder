def main():
  N = int(input())
  a = list(map(int, input().split()))

  c = [0] * (max(a)+3)

  for v in a:
    c[v+1] += 1

  ans = 0

  for i in range(1, len(c) - 1):
    x = c[i-1] + c[i] + c[i+1]
    ans = max(ans, x)

  print(ans)

if __name__ == "__main__":
  main()