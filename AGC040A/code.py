def main():
	S = input()
	h = [0] * (len(S) + 1)

	#  <  となっている場合だけを考える
	# a[i] < a[i+1] でない場合、a[i] に +1 したものを a[i+1] にする
	for i in range(len(S)):
		if(S[i] == "<"):
			h[i+1] = max(h[i+1], h[i] + 1)

	# > となっている場合だけを考える
	# a[i-1] > a[i] でない場合、a[i] に +1 したものを a[i-1] にする
	# この時この操作は逆順から行う
	for i in range(len(S), 0, -1):
		if(S[i-1] == ">"):
			h[i-1] = max(h[i-1], h[i] + 1)

	print(sum(h))

if __name__ == "__main__":
	main()