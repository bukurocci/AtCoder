def main():
  N = int(input())
  a = [0] * N
  visited = [False] * N
  l = 0
  ans = 0


  for i in range(N):
    a[i] = int(input())

  visited[0] = True

  while(l != 1):
    l = a[l] - 1

    if(visited[l]):
      ans = -1
      break
    
    visited[l] = True
    ans += 1

  print(ans)

if __name__ == "__main__":
  main();