def main():
  X, N = list(map(int, input().split()))

  ans = X;
  min_value = 204

  if N == 0:
    print(ans)
  else:
    p = list(map(int, input().split()))
    a = [i for i in range(0, 204)]

    for v in p:
      a[v] = -1

    for i in range(0, 204):
      if a[i] != -1:
        d = abs(X - a[i])

        if(min_value > d):
          min_value = d
          ans = i

    print(ans);

if __name__ == '__main__':
  main()