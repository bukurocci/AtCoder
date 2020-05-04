N = int(input())

answer = "No"

for i in range(1, 10):
  should_break = False
  for j in range(1, 10):
    if(i * j == N):
      answer = "Yes"
      should_break = True
      break

  if(should_break):
    break

print(answer)