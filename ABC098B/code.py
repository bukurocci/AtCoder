from string import ascii_lowercase 

def main():
  N = int(input())
  S = input()

  ans = 0

  for i in range(1, N-1):
    left = S[:i]
    right = S[i:]

    letters = []
    for c in ascii_lowercase:
      if(c in left):
        letters.append(c)

    count = 0
    for c in letters:
      if c in right:
        count += 1

    ans = max(ans, count)

  print(ans)

if __name__ == "__main__":
  main()