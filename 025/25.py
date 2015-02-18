f,s,t,i=1,1,0,2
while str(t).__len__()<1000:
	t=f+s
	f,s=s,t
	i+=1
print(i)