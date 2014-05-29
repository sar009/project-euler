num=0
for i in range(2, 600851475143+1, 1):
	if(600851475143%i==0):
		k=int(600851475143/i)
		for j in range(2, k+1, 1):
			if (k%j==0):
				if (k==j):
					num=k
				break
	if (num>0):
		break
print(num)