#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857
#

num = 0
i = 0
while i < 600851475143:
	i += 1
	if (600851475143%i == 0):
		k = int(600851475143/i)
		j = 0
		while j < k+1:
			j += 1
			if k%j == 0:
				if k == j:
					num=k
				break
	if num > 0:
		break
	print i
print num