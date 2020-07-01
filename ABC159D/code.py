def main():
  N = int(input())
  A = list(map(int, input().split()))

  counts = [0] * N

  for v in A:
    counts[v-1] += 1

  total = 0

  for v in counts:
    if(v > 1):
      total += v * (v - 1) // 2

  for v in A:
    n = counts[v-1]

    diff = n * (n - 1) // 2 - (n-1) * (n-2) // 2

    print(total - diff)


if __name__ == "__main__":
  main()