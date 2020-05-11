from itertools import combinations

def main():
    N, M, X = list(map(int, input().split()))

    row = []

    ans = 10 ** 10

    for i in range(N):
        row.append(list(map(int, input().split())))

    for k in range(1, N+1):
        co = list(combinations(row, k))

        for t in co:
            cost = 0
            skill = [0] * M
            for v in t:
                cost += v[0]
                for s in range(M):
                    skill[s] += v[s+1]

            if(min(skill) >= X):
                ans = min(ans, cost)

    if(ans == 10 ** 10):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()