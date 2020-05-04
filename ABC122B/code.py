def is_acgt_char(c):
  return c == "A" or c == "C" or c == "G" or c == "T"

def main():
  S = input()
  ans = 0

  for i in range(len(S)):
    count = 0
    
    for j in range(i, len(S)):
      if(not is_acgt_char(S[j])):
        break

      count += 1

    ans = max(ans, count)

  print(ans)

if __name__ == "__main__":
  main()