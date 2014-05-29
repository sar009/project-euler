sum=0
a=[]
def ami(num):
	p=0
	for j in range(1, num, 1):
		if (num%j==0):
			p+=j
	return p
for i in range(0, 10001, 1):
	a.append(i)
	a[i]=0
for i in range(1, 10001, 1):
	f,s=0,0
	if (a[i]==0):
		f=ami(i)
		s=ami(f)
	if (s==i and f!=s):
		a[i]=f
		if (f<10001):
			a[f]=s
	if (i%100==0):
		print(i)
for i in range(0, 10001, 1):
	if(a[i]!=0):
		sum+=a[i]
print(sum)