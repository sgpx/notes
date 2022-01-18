#!/usr/bin/env python3
import subprocess as s
import json
import datetime
from sys import argv,exit

nlg, nls = None, None

if len(argv) >= 3:
	_, nlg, nls = argv[:3]
	nlg = int(nlg)
	nls = int(nls)


def execute(cmd):
	x = s.check_output(cmd.split(" "))
	x = x.decode("utf-8")
	x = json.loads(x)
	return x

cmd = "aws logs describe-log-groups"
x = execute(cmd).get("logGroups")

print("=======")
print("groups:")
for n,i in enumerate(x):
	print(n+1,"->",i.get("logGroupName"))
print("=======")

if nlg:
	p = nlg - 1
else:
	p = int(input("enter number of log group: ")) - 1
log_group_name = x[p].get("logGroupName")

cmd = f"aws logs describe-log-streams --log-group-name {log_group_name}"
x = execute(cmd).get("logStreams")

print("=======")
print("streams:")
print("=======")
for n,i in enumerate(x):
	print(n+1,"->", i.get("logStreamName"), "# created at: ", str(datetime.datetime.fromtimestamp(i.get("creationTime")/1000)) )
print("=======")

if nls:
	p = nls - 1
else:
	p = int(input("enter number of log stream: ")) - 1
log_stream_name = x[p].get("logStreamName")

print("=======")
cmd = f"aws logs get-log-events --log-group-name {log_group_name} --log-stream-name {log_stream_name}"
x = execute(cmd).get("events")
print(x)

for i in x:
	print("\n=== event ===\n")
	for j in i:
		print(j,":",i[j])
