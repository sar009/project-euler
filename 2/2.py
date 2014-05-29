sum=2
f=1
s=2
t=0
while t<4000000:
	t=f+s
	f=s
	s=t
	if t%2==0:
		sum+=t
print(sum)