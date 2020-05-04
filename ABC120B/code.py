def main():
  A,B,K = list(map(int, input().split()))
  o = 0

  for i in range(min(A, B), 0, -1):
    if(A % i == 0 and B % i == 0):
      o += 1

      if(K == o):
        print(i)
        break
    

if __name__ == "__main__":
  main()