a, b = list(map(int, input().split()))

print(["Even", "Odd"][(a * b) % 2])