num=grt=1

def collatz(no):
	if no==1:
		return 1
	else:
		if no%2==0:
			return 1+collatz(int(no/2))
		else:
			return 1+collatz((3*no)+1)
			
for i in range(2, 1000000, 1):
	a=collatz(i)
	if (a>grt):
		num=i
		grt=a
	if (i%1000==0):
		print(i)
print(num)