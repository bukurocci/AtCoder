N = int(input())

dic = {}

for _ in range(N): 
  s = input()

  if(s in dic) :
    dic[s] += 1
  else:
    dic[s] = 1
  


print(len(dic))
