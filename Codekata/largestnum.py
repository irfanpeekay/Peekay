i, r, f = raw_input().split()
i= int(i)
r=int(r)
f=int(f)
if (i>=r) and (i>f):
	print i
elif (r>=i) and (r>f):
	print r
else:
	print f
