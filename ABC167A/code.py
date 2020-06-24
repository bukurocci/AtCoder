def main():
    S = input()
    T = input()

    if(T[0:len(T)-1] == S):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()