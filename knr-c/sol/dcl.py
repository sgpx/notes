a = input(">>> ")
print(a)

output = ""
token = ""
name = ""

def gettoken():
	return "\n"


def dirdcl():
	if tokentype == "(":
		dcl()
		if tokentype != ")":
			print("missing ')'\n")

	elif tokentype == "NAME":
		name = token
	else:
		print("expected name or dcl\n")

	type = gettoken()
	while type in ["PARENS", "BRACKETS"]:
		if type == "PARENS":
			output += " function returning"
		else:
			output += " array "
			output += token
			output += " of "
def dcl():
	ns = 0
	while gettoken() == "*":
		ns += 1

	dirdcl()

	for i in range(ns):
		output += "pointer to "

	
def main():
	pass

if __name__ == "__main__":
	main()
