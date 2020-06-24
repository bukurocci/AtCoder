def main():
  A = int(input())
  ans = -1

  for k in range(10, 10001):
    x = k
    a = 0
    d = 1

    while x != 0:
      m = (x % 10)
      a += m * d

      x //= 10
      d *= k

    if(a == A):
      ans = k
      break

  print(ans)

if __name__ == "__main__":
  main()