N, K = list(map(int, input().split()))

res = []

while True:
    if N < K:
        break

    m = N % K
    div = N // K

    res.append(m)

    N = div

print(len(res) + 1)