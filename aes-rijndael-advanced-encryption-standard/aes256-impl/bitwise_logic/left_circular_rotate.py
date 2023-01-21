import math

def p(x):
	return 2**(int(math.log(x,2)))
	# (power of 2 closest to x) or 2**(number of bits - 1)

def left_circular_shift(x):
	a = x
	print("===")
	print(bin(a), a)
	rem = a - p(a)
	print(bin(rem), rem)
	rem = rem << 1
	print(bin(rem), rem)
	rem = rem | 1
	print(bin(rem), rem)
	return rem

a = 0b101101101
a = left_circular_shift(a)
a = left_circular_shift(a)

