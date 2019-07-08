def prime(n):
	if(n>1):
		for i in range(2, n):
			if(n%i == 0):
				return "no"
			else:
				return "yes"
	else:
		return "no"
		
n = int(input(""))
print(prime(n))
