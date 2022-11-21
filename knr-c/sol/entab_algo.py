a =  "a..b....c"
a += "a.......c"
#a = "a.......c"
a += "a.....b.c"
#a = "a.....b.c"

b = ""
i = 0
wsc = 0

ts = 8

while i != len(a):
	c = a[i]
	if ts == 0:
		ts = 8
		if wsc:
			b += '\t'
			wsc = 0
	if c == '.':
		wsc += 1
	else:
		if wsc:
			apn = '.'*wsc
			b += apn
			wsc = 0
		b += c			
	i += 1
	ts -= 1

print(a)
print(b)
