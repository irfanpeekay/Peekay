def palindrome(n):
	tem = n
	d = 0
	r = 0
	
	while (n>0):
		d = n % 10 
		r = r * 10 + d
		n = n // 10
	if(tem == r):
		return "yes"
	else:
		return "no"
			
n = int(input(""))
print(palindrome(n))
