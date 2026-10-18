#!/usr/bin/env python3

gc_buf = None
gc_ctr = 0


def getchar():
    global gc_buf, gc_ctr

    if gc_buf == None:
        gc_buf = input(">>> ") + "\n"
        gc_ctr = 0

    res = gc_buf[gc_ctr]
    gc_ctr += 1

    if gc_ctr == len(gc_buf):
        gc_buf = None

    return res


gh_buf_size = 1024
gh_buf = [' '] * gh_buf_size
gh_ctr = 0


def getch():
    global gh_buf, gh_ctr
    if gh_ctr > 0:
        gh_ctr -= 1
        return gh_buf[gh_ctr]
    else:
        return getchar()


def ungetch(x):
    global gh_buf, gh_ctr
    gh_buf[gh_ctr] = x
    gh_ctr += 1


debugmode = 1

EOL = '#'

pr_token = ""
pr_name = ""
pr_datatype = ""
pr_out = ""
pr_tokentype = ""


def reset():
    global pr_token, pr_name, pr_datatype, pr_out, pr_tokentype
    pr_token = ""
    pr_name = ""
    pr_datatype = ""
    pr_out = ""
    pr_tokentype = ""


def prdef():
    global pr_token, pr_name, pr_datatype, pr_out, pr_tokentype
    return
    print("=========")
    print("pr_token", pr_token)
    print("pr_tokentype", pr_tokentype)
    print("pr_name", pr_name)
    print("pr_datatype", pr_datatype)
    print("pr_out", pr_out)
    print("=========")


cyc_buf = ""

def cyc_print(x):
	global cyc_buf
	cyc_buf += x + " > "
	print(cyc_buf)

def dbg_print(*args):
    global debugmode
    if debugmode:
        print(" ".join([str(i) for i in args]))


def dcl():
    cyc_print("dcl")

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
    cyc_print("dirdcl")

    global pr_name, pr_token, pr_out, pr_tokentype
    type = None
    prdef()
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
    cyc_print("gettoken")
    global pr_name, pr_token, pr_tokentype
    pr_token = ""
    c = getch()

    while c == ' ':
        c = getch()

    dbg_print("c:", repr(c))

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
                raise Exception(
                    "error: reached EOL without closing bracket ']'\n")
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
        #print("returning NAME pr_token", pr_token)
        pr_tokentype = "NAME"
        return pr_tokentype
    else:
        pr_tokentype = c
        return pr_tokentype


tok = gettoken()
while tok != EOL:
    #print("tok:", tok)
    prdef()

    pr_datatype = pr_token
    out = ""

    dcl()

    if pr_tokentype != "\n":
        print("syntax error\n")

    #if tok == "NAME":
    print("{} : {} {}".format(pr_name, pr_out, pr_datatype))
    reset()
    tok = gettoken()
    cyc_buf = ""
