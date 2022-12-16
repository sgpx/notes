#!/usr/bin/env python3
debugmode = 1

EOL = "\0"

pr_token = ""
pr_name = ""
pr_datatype = ""
pr_out = ""

input_line = input(">>> ") + EOL
ctr = 0

def dbg_print(*args):
	global debugmode
	if debugmode:
		print(" ".join([str(i) for i in args]))

def getch():
	global input_line, ctr

	if ctr < len(input_line):
		res = input_line[ctr]
		ctr += 1
		return res
	else:
		return EOL

def ungetch(*args):
	global ctr

	if ctr > 0:
		ctr -= 1

def dcl():
	global pr_name, pr_token, pr_out

	ns = 0
	xtok = gettoken()
	while xtok == '*':
		ns += 1
		xtok = gettoken()

	dirdcl()

	for i in range(ns):
		pr_out += " pointer to "

def dirdcl():
	global pr_name, pr_token, pr_out, pr_tokentype
	type = None

	if pr_tokentype == "(":
		dcl()
		if pr_tokentype != ')':
			raise Exception("error: missing closing parenthesis\n")
	elif pr_tokentype == "NAME":
		pr_name = pr_token
	else:
		raise Exception("error: expected name or dcl()\n")

	type = gettoken()
	while type == "PARENS" or type == "BRACKETS":
		if type == "PARENS":
			pr_out += " function returning "
		else:
			pr_out += " array "
			pr_out += pr_token
			pr_out += " of "

		type = gettoken()
	return

def gettoken():
	global pr_name, pr_token, pr_tokentype
	pr_token = ""
	c = getch()
	# dbg_print("c:", c)

	while c == ' ':
		c = getch()

	if c == '(':
		c = getch()

		if c == ')':
			dbg_print("c:", c)
			pr_tokentype = "PARENS"
			return pr_tokentype
		else:
			ungetch(c)
			pr_tokentype = '('
			return pr_tokentype

	elif c == '[':
		pr_token += c
		c = getch()
		while c != ']':
			if c == EOL:
				raise Exception("error: reached EOL without closing bracket ']'\n")
				pr_tokentype = EOL
				return pr_tokentype
			pr_token += c
			c = getch()

		pr_token += c

		dbg_print("pr_token", pr_token)
		pr_tokentype = "BRACKETS"
		return pr_tokentype

	elif c.isalpha():
		while c.isalnum():
			pr_token += c
			c = getch()
		ungetch(c)
		pr_tokentype = "NAME"
		return pr_tokentype
	else:
		pr_tokentype = c
		return pr_tokentype


tok = gettoken()
while tok != EOL:
	print("tok:", tok)

	pr_datatype = pr_token
	out = ""

	dcl()


	if tok == "NAME":
		print("pr_token", pr_token)
	print("{} : {} {}".format(pr_name, pr_out, pr_datatype))
	tok = gettoken()
