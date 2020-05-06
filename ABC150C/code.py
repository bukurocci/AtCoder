import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

pi = 0
qi = 0

def dfs(array, n):
  if(len(array) == n):
    return [tuple(array)]

  ret = []

  # 再起処理
  for i in range(1, N+1):

    if(i in array):
      continue

    array.append(i)
    ret.extend(dfs(array, n))
    array.pop()

  return ret


for index, pattern in enumerate(dfs([], N)):
  if P == pattern:
    pi = index
  if Q == pattern:
    qi = index

print(abs(pi - qi))
