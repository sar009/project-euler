sum=2
i=3
num=[]
num.append(2)
while (i<2000000):
	flag=0
	for j in range(0, num.__len__(), 1):
		if (i%num[j]==0):
			flag=1
			break
	if(flag==0):
		num.append(i)
		sum+=i
	i+=1
print(sum)

#142913828922
