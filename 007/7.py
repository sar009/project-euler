count=1
i=2
while (count<=10001):
	for j in range(2, i+1, 1):
		if (i%j==0):
			if (i==j):
				count+=1
			break
	i+=1
print(i-1)