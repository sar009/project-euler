num=1
sum=0
for i in range(100, 1, -1):
	num*=i
num=str(num)
for i in range(0, num.__len__(), 1):
	sum+=int(num[i])
print(sum)