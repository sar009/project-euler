file=open("13.txt", "r")
a=file.readlines()
file.close()
sum=0
for i in range(0, 100, 1):
	sum+=int(a[i])
print(sum)