N = int(input())
nums = list(map(int, input().split()))
min_op = 10 ** 9;

for i in range(N):
  x = nums[i]
  op = 0

  while(x % 2 == 0):
    op += 1
    x //= 2

  if(min_op > op):
    min_op = op

print(min_op)