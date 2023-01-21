import math

def check(x):
	return int(1+math.log(x, 2)) == (len(bin(x)) - 2)

for i in range(1, 100000):
	if not check(i):
		print(i)
		break


