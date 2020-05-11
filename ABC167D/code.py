from queue import Queue

def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    visited = [False] * N
    visited[0] = True
    p = [1]
    l = []
    r = []

    while(len(p) < N):
        v = p[-1] - 1
        n = A[v] - 1

        if(visited[n]):
            d = p.index(n+1)
            l = p[0:d]
            r = p[d:]
            break

        p.append(A[v])
        visited[n] = True

    if(len(l) == 0 and len(r) == 0):
        print(p[K%len(p)])
    else:
        if(K < len(p)):
            print(p[K])
        else:
            k = K - len(l)
            k %= len(r)
            print(r[k])
        

if __name__ == "__main__":
    main()