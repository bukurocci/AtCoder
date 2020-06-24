import string

def main():
  N = int(input())
  az = string.ascii_lowercase
  d = 26
  ans = ""

  while(N > 0):
    m = (N-1) % d
    ans = az[m] + ans
    N = (N-1) // d
    
  print(ans)


if __name__ == "__main__":
  main()