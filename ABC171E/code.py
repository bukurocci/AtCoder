def main():
  N = int(input())
  A = list(map(int, input().split()))

  X = A[0]

  for i in range(1, N):
    X = X ^ A[i]

  B = []

  for v in A:
    B.append(X ^ v)
  
  print(" ".join(map(str, B)))

if __name__ == "__main__":
  main()