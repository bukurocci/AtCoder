
def main():
  N = int(input())
  S = input()

  ans = 0

  # PINの方のパターンが少ないので、PINが文字列から再現できるか全探索する
  for i in range(1000):
    pin = str(i).zfill(3)
    cur = 0

    for char in S:
      if(pin[cur] == char):
        cur += 1

        if(cur == 3):
          ans += 1
          break;

  print(ans)


if __name__ == "__main__":
    main()