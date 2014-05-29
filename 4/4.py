num=0
for i in range(998001, 0, -1):
	a=str(i)
	b=a[::-1]
	if (a==b):
		j=999
		while (999*j>=i):
			if (i%j==0):
				num=i
				break
			j-=1
		if (num>0):
			break
print(num)