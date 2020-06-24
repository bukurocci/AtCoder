def main():
	H,W = list(map(int, input().split()))
	grid = []

	for _ in range(H):
		grid.append(list(input()))

	shift = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

	for i in range(H):
		for j in range(W):
			if(grid[i][j] == "#"):
				continue
			
			count = 0
			for k in shift:
				ii = i + k[0]
				jj = j + k[1]

				if(-1 < ii < H and -1 < jj < W and grid[ii][jj] == "#"):
					count += 1
			
			grid[i][j] = count

	for row in grid:
		print("".join(map(str, row)))


if __name__ == "__main__":
	main()