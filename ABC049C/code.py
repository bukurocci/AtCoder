S = str(input())[::-1]
pos = 0
words = [s[::-1] for s in ["dream", "dreamer", "erase", "eraser"] ]
res = "YES"

while True:
  if(pos >= len(S)): break

  ok = False
  for word in words:
    if(S[pos:pos+len(word)] == word):
      ok = True
      pos += len(word)
      break

  if(not ok):
    res = "NO"
    break

print(res)

