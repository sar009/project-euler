num=str(2**1000)
sum=0
for i in range(0, num.__len__(), 1):
	sum+=int(num[i])
print(sum)