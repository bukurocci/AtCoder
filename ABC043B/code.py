def main():
  s = input()

  ans = ""

  for c in s:
    if(c == "0"):
      ans += "0"
    elif(c == "1"):
      ans += "1"
    elif(c == "B"):
      if(ans != ""):
        ans = ans[0:len(ans) - 1]

  print(ans)

if __name__ == "__main__":
    main()