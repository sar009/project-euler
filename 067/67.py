file=open("67.txt", "r")
a=[[int(val) for val in line.split()] for line in file.readlines()]
file.close()
b=a[-1]
c=size=a.__len__()-1
for i in range(size-1, -1, -1):
	for j in range(0, c, 1):
		if (a[i][j]+b[j]>a[i][j]+b[j+1]):
			b[j]=a[i][j]+b[j]
		else:
			b[j]=a[i][j]+b[j+1]
	c-=1
print(b[0])