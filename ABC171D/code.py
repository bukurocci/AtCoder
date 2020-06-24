def main():
  N = int(input())
  A = list(map(int, input().split()))
  Q = int(input())

  MAX = 10 ** 5

  total = sum(A)
  counts = [0] * (MAX + 1)

  for v in A:
    counts[v] += 1

  for _ in range(Q):
    B, C = list(map(int, input().split()))
    diff = C - B
    t = counts[B]
    counts[B] = 0
    counts[C] += t

    total += diff * t
    print(total)

if __name__ == "__main__":
  main()