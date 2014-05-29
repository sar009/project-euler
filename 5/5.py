num=1
for i in range(1, 20, 1):
	j=1
	while (num%i!=0):
		num*=j
		if (num%i!=0):
			num/=j
		j+=1
print(num)