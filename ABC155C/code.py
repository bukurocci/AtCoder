N = int(input())
dict = {}
max_count = 0
max_count_words = []

for _ in range(N):
  s = str(input())

  if(s in dict):
    dict[s] += 1
  else:
    dict[s] = 1

for key, value in dict.items():
  if(value > max_count):
    max_count = value
    max_count_words = [key]
  elif(value == max_count):
    max_count_words.append(key)

list.sort(max_count_words)
print("\n".join(map(str, max_count_words)))