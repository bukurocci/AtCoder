import math
A,B,C,D = list(map(int, input().split()))

turn_t = math.ceil(C / B);
turn_a = math.ceil(A / D);

print("No" if turn_t > turn_a else "Yes")