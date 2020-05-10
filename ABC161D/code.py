from queue import Queue

def main():
	K = int(input())
	count = 0
	ans = 0

	q = Queue()
	q.put(-1)


	while(not q.empty()):
		next_loop = True
		v = q.get()

		if(v == -1):
			for i in range(1, 10):
				q.put(i)
				count += 1

				if(count == K):
					ans = i
					next_loop = False
				
		else:
		
			for i in range(0, 10):
				d1 = v%10
				
				if(not (d1-1 <= i <= d1+1)):
					continue

				count += 1

				if(count == K):
					ans = v * 10 + i
					next_loop = False
					break

				q.put(v * 10 + i)
		
		if(not next_loop):
			break

	print(ans)


if __name__ == "__main__":
	main()