p=sum=1
for i in range(3, 1001+1, 2):
	n=i*i
	s=((n-p)/2)+p
	t=(n-s)/2
	t1=s-t
	t2=s+t
	sum+=n+s+t1+t2
	p=n
print(sum)