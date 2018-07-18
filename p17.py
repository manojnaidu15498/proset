n,k=input().split()
if n.isdigit() and k.isdigit():
	n=int(n)
	k=int(k)
	z=input().split()
	s=0
	def add():
		h=0
		for i in range(0,n):
			x=int(z[i])
			for j in range(0,n):
				if(i==j):
					continue
				else:
					w=x+int(z[j])
					if w==k:
						h=h+1
		if h>0:
			print("yes")
		else:
			print("no")
	for i in range(0,len(z)):
		if z[i].isdigit():
			s=s+1
	if len(z)==n:
		if s==n:
			add()
	elif n>len(z):
		n=len(z)
		if s==n:
			add()
	else:
		add()
else:
	print ("Invalid")
