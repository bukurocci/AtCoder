N,A,B = list(map(int, input().split()))

# 1ターンで追加されるボールのかず
append_per_turn = A + B

d = N // append_per_turn
m = N % append_per_turn

print(A * d + min(A, m))


