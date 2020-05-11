def main():
    A, B, C, K = list(map(int, input().split()))

    rest = K
    total = 0

    if(rest - A >= 0):
        rest = max(0, rest - A) 
        total += 1 * A
    else:
        total += 1 * rest

    rest = max(0, rest - B) 

    
    total += -1 * rest

    print(total)

if __name__ == "__main__":
    main()