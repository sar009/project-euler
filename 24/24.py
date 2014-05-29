num,count,fnum="0123456789",0,""
def chk(n):
	for i in range(0, 10, 1):
		for j in range(i+1, 10, 1):
			if (n[i]==n[j]):
				return False
	return True
while(count<1000000):
	if (num.__len__()<10):
		num="0"+num
	if (chk(num)):
		count+=1
	fnum=num
	num=str(int(num)+9)
print(fnum)
#2783915460