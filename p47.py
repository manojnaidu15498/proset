a,b=input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	def ans():
		i=1
		e=10**b
		while(i<a):
			m=a*i
			i=i+1
			if m%a==0:
				if m%e==0:
					print(m)
					break
	def ans1():
		i=1
		e=10**b
		while(i<a):
			m=a*i
			i=i*10
			if m%a==0:
				if m%e==0:
					print(m)
					break
	if b<6:
		ans()
	else:
		ans1()
else:
	print("Invalid")
