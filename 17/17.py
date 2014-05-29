num=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
b=""
for i in range(1,100,1):
	a=i
	c=False
	if (str(a).__len__()==4):
		b+="onethousand"
		break;
	if (str(a).__len__()==3):
		b+=num[int(a/100)]+"hundred"
		c=True
		a=a%100
	if (str(a).__len__()<=2):
		if (a>0 and a<20):
			if c:
				b+="and"
			b+=num[a]
		elif (a>19):
			if c:
				b+="and"
			b+=num[int(a/10)+18]
			a=a%10
			if (a>0 and a<10):
				b+=num[a]
print(b.__len__())