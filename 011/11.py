file=open("11.txt", "r")
a=[[int(val) for val in line.split()] for line in file.readlines()]
file.close()
pro=0
for i in range(0, 20, 1):
	j=0
	while (j+3<20):
		tempro=a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
		if (tempro>pro):
			pro=tempro
		tempro=a[j][i]*a[j+1][i]*a[j+2][i]*a[j+3][i]
		if (tempro>pro):
			pro=tempro
		j+=1
for i in range(16, -1, -1):
	j=0
	while (j+3<20):
		tempro=a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
		if (tempro>pro):
			pro=tempro
		j+=1
for i in range(1, 17, 1):
	j=0
	while (j+3<20):
		tempro=a[j][i]*a[j+1][i+1]*a[j+2][i+2]*a[j+3][i+3]
		if (tempro>pro):
			pro=tempro
		tempro=a[j][i]*a[j+1][i-1]*a[j+2][i-2]*a[j+3][i-3]
		if (tempro>pro):
			pro=tempro
		j+=1
for i in range(3, 20, 1):
	j=0
	while (j+3<20):
		tempro=a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3]
		if (tempro>pro):
			pro=tempro
		j+=1
print(pro)