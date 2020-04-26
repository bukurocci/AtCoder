N = int(input())
S = input()

total = 0
m = 0

for j in range(1, N):

    ic = {
        "R": 0,
        "G": 0,
        "B": 0
    }

    kc = {
        "R": 0,
        "G": 0,
        "B": 0
    }

    m = 0

    for i in range(j-1, -1, -1):
        ic[S[i]] += 1
    
    for k in range(j+1, N):
        kc[S[k]] += 1

    for l in range(min(j+1, N-j)):
        if(S[j - l] != S[j + l] and S[j] != S[j + l] and S[j] != S[j - l]):
            m += 1

    if(S[j] == "R"):
        total += ic["G"] * kc["B"] + ic["B"] * kc["G"]
    elif(S[j] == "G"):
        total += ic["R"] * kc["B"] + ic["B"] * kc["R"]
    elif(S[j] == "B"):
        total += ic["R"] * kc["G"] + ic["G"] * kc["R"]

    total -= m

print(total)