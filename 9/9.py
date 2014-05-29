num=0
for i in range (332, 0, -1):
	for j in range (int((1000-i)/2), i+1, -1):
		k=1000-i-j
		if ((i*i)+(j*j)==k*k):
			num=i*j*k
			print(i)
			print(j)
			print(k)
			break
	if (num>0):
		break
print(num)
