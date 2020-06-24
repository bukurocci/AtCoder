
def main():
	S = input()
	n = len(S)
	ans = 0

	black = 0
	f_pos = 0
	l_pos = 0

	for i, c in enumerate(S):
		if(c == 'B'):			
			f_pos += i
			black += 1

	l_pos = sum(list(range(n-1, n-1-black, -1)))
	

	ans = l_pos - f_pos

		
	print(ans)

if __name__ == "__main__":
	main()