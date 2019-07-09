def armstrong_btw(x, y):
	for n in range(x, y):
		sum = 0
		t = n
		p = len(str(n))
		while(t>0):
			d = t%10
			sum=sum+d**p
			t=t//10
		if(n==sum):
			print(n, end=" ")
		
a, b= map(int, input().split())
armstrong_btw(a, b)
