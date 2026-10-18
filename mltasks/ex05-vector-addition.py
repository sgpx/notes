# id,exercise_name,topic,subject,chapter_number,chapter
# 1,Implement vector addition and dot product in pure Python,Vectors and dot products,Math Foundations,1,Linear Algebra

class myvector:
	def __init__(self, *args):
		vals = {}
		for n,i in enumerate(args):
			if type(i) == int: vals[n] = i
		self.vals = vals

	def __add__(self, x):
		rv = myvector()
		for z in [self, x]:
			for n in sorted(list(z.vals)):
				i = z.vals[n]
				if type(i) == int:
					rv.vals[n] = rv.vals.get(n, 0) + z.vals.get(n, 0)
		return rv

	def __mul__(self, x):
		rv = 0
		z1 = list(self.vals.keys())
		z2 = list(x.vals.keys())
		z3 = set(z1+z2)
		for i in z3:
			rv += (self.vals.get(i,0) * x.vals.get(i,0))
		return rv

	def __str__(self):
		tmp = ""
		for n in sorted(list(self.vals)):
			tmp += f"{self.vals[n]} "
		return tmp.strip()


vec1 = myvector(1,3,4)
vec2 = myvector(3,2,3)

print(vec1 + vec2)
