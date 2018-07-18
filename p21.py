n=input()
if(n.isdigit()):
	n=int(n)
	z=0
	a=input().split()
	l=[]
	for i in range(0,n):
		l.append(int(a[i]))
		z=z+int(a[i])
	su=0
	sumb=0
	m=0
	for i in range(0,n-1):
		avg=0
		avg2=0
		su=su+l[i]
		sumb=z-su
		avg=su/(i+1)
		avg2=sumb/(n-i-1)
		if avg==avg2:
			m=1
			print("yes")
			break
		else:
			continue
if m==0:
	print("no")
