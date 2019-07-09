def armstrong(n):
	sum = 0
	temp = n
	p = len(str(n))
	while(temp>0):
		d = temp % 10
		sum = sum + d ** p
		temp = temp // 10
	if(n == sum):
		return "yes"
	else:
		return "no"
		
a = int(input(""))
print(armstrong(a))
