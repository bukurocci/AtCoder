def main():
  N = int(input())
  ans = 0
  
  for i in range(3, N+1, 2): #1は調べる必要がない
    count = 2 # 1と自分

    for j in range(3, (N + 1) // 2, 2):
      if(i % j == 0):
        count += 1
      
    if(count == 8):
      ans += 1

  print(ans)

if __name__ == "__main__":
  main()