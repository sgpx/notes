lines = open("a.log","r").read().split("\n")

a = lines[0].split(",")
print(a)
for i in lines[1:]:
	b = i.split(",")
	for n,j in enumerate(b):
		print(a[n], ":", j)
	print("===")
