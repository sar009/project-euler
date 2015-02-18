import winsound
num=0
#5400 8152
i=8000
while(num<500):
	count=1
	a=int((i*(i+1))/2)
	for j in range(1, int((a+2)/2), 1):
		if (a%j==0):
			count+=1
	if (count>num):
		num=count
	i+=1
	print(i)
	print(num)
print(int((i*(i-1))/2))
for j in range(1, 10, 1):
	winsound.Beep(1000, 500)
	winsound.Beep(2000, 500)
	winsound.Beep(3000, 500)
	winsound.Beep(2000, 500)