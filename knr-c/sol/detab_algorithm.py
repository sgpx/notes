a = "asdf\tewrs\t\t\twerwefw\t\tx"
b = ""
tab_array = []

i = 0
tc = 0
typed = 0

while i < len(a):
	print(i)
	c = a[i]
	if c == '\t':
		if tc < len(tab_array):
			cts = tab_array[tc]
			tc += 1
		else:
			cts = 8
		ns = cts - typed
		print("ns", ns)
		apn = " " * ns
		b += apn
		typed = 0
	else:
		typed += 1
		b += c
	i += 1

print(repr(a))
print(a)
print(b)
