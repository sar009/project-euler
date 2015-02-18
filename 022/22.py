file=open("22.txt", "r")
a=file.readlines()[0].strip("\"").split("\",\"")
file.close()
for i in range(0, len(a), 1):
	for j in range(i+1, len(a), 1):
		if (a[i]>a[j]):
			temp=a[i]
			a[i]=a[j]
			a[j]=temp
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum=0
for i in range(0, len(a), 1):
	val=0
	for j in range(0, a[i].__len__(), 1):
		val+=alph.index(a[i][j])+1
	val*=i+1
	sum+=val
print(sum)