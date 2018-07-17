inpu=int(input())
z=[]
for i in range(0,inpu):
	y=input()
	z.append(y)
n=len(z)
l=[]
e=[]
for i in range(0,n-1):
	s=z[0]
	f=z[i+1]
	q=len(s)
	t=len(f)
	if q>t:
		o=t
	elif q<t:
		o=q
	elif q==t:
		o=q
	for j in range(0,o):
		if(s[j]==f[j]):
			l.append(f[j])
		else:
			break
	r=("".join(l))
	e.append(r)
	l=[]
h=len(e)
w=[]
m=[]
if(h==1):
	print(e[0])
else:
	for i in range(0,h-1):
		s=e[0]
		f=e[i+1]
		q=len(s)
		t=len(f)
		if(q>t):
			o=t
		elif(q<t):
			o=q
		elif(q==t):
			o=q
		for j in range(0,o):
			if(s[j]==f[j]):
				w.append(f[j])
			else:
				break
		r=("".join(w))
		m.append(r)
		w=[]
	print(m[0])
