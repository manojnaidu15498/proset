a,b=input().split()
a=int(a)
b=int(b)
c=[]
m='R'
n='G'
for i in range(0,a):
	d=input()
	c.append(d)
e=[]
sum=0
for i in range(0,a):
	t=c[i]
	for j in range(0,b):
		e.append(t[j])
	for j in range(0,b-1):
		if e[j]==e[j+1]:
			if e[j]==m:
				e[j]=n
				sum=sum+5
			else:
				e[j]=m
				sum=sum+3
	e=[]
print(sum)
