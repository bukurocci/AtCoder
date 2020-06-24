def main():
	S = input()
	ans = 0
	while(len(S) > 0):
		l = len(S) - 1
		S = S[0:l]

		if(l%2 == 0):
			left = S[0:l//2]
			right = S[l//2:]

			if(left == right):
				ans = l
				break

	print(ans)

if __name__ == "__main__":
	main()