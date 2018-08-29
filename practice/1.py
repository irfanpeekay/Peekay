a, b, c, d, e, f = map(int, raw_input().split())
if (a>b) and (a>c) and (a>d) and (a>e) and (a>f):
	largest_num = a
elif (b>a) and (b>c) and (b>d) and (b>e) and (b>f):
	largest_num = b
elif (c>a) and (c>b) and (c>d) and (c>e) and (c>f):
	largest_num = c
elif (d>a) and (d>b) and (d>c) and (d>e) and (d>f):
	largest_num = d
elif (e>a) and (e>b) and (e>c) and (e>d) and (e>f):
	largest_num = e
else:
	largest_num = f
print (largest_num)
