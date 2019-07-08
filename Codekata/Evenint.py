def evenbtw(n, k):
	for i in range(n+1, k):
		if(i%2 == 0):
			print(i, end = " ")

a, b= map(int, input().split())
evenbtw(a, b)
