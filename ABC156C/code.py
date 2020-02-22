N = int(input())
X = list(map(int, input().split()))

min_power = 1000001

for p in range(1, 100+1):
    total = 0

    for value in X:
       total += (value - p) ** 2

    if total < min_power:
        min_power = total

print(min_power)