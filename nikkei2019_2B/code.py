def main():
  N = int(input())
  D = list(map(int, input().split()))
  print(max(D))
  c = [0] * (N - 1)
  ans = 1

  for value in D:
    c[value] += 1

  print(ans)

if __name__ == "__main__":
  main()