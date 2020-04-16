K = int(input())
total = 0

def gcd(a, b):
    if(a > b):
        a, b = b, a

    while(b > 0):
        r = a % b
        a = b
        b = r

    return a

dp = [[0 for i in range(K+1)] for j in range(K+1)]

for a in range(1, K+1):
    for b in range(1, K+1):
        if(dp[a][b] == 0):
            dp[a][b] = gcd(a, b)

        res = dp[a][b]

        for c in range(1, K+1):
            if(dp[res][c] == 0):
                dp[res][c] = gcd(res, c)

            total += dp[res][c]


print(total)