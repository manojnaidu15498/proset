a=input().split()
b=input().split()
c=input().split()
d=input().split()
if a[0].isdigit() and a[1].isdigit():
	if b[0].isdigit() and b[1].isdigit():
		if c[0].isdigit() and c[1].isdigit():
			if d[0].isdigit() and d[1].isdigit():
				if a[0]==b[0]:
					m=int(a[1])-int(b[1])
					m=abs(m)
				else:
					m=0
				if a[1]==d[1]:
					p=int(a[0])-int(d[0])
					p=abs(p)
				else:
					p=0
				if b[1]==c[1]:
					n=int(b[0])-int(c[0])
					n=abs(n)
				else:
					n=0
				if c[0]==d[0]:
					o=int(c[1])-int(d[1])
					o=abs(o)
				else:
					o=0
				if(m==n==o==p):
					print("yes")
				else:
					print("no")
