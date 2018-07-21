a=input()
b=input()
i=1
n=len(a)
m=len(b)
if(n>m):
        g=m
        h=b
        j=a
else:
        g=n
        h=a
        j=b
while i<g:
	d=h*i
	if d==j:
		print(i)
	i=i+1
