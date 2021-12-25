#!/usr/bin/env python3
import psutil as p
import os

while True:
	a = [i for i in p.process_iter() if i.cmdline() and "Z:" in i.cmdline()[0]]
	if a:
		print(a[0].cmdline())
		pid = a[0].pid
		print("found pid",pid)
		os.system(f"strace -xx -y -v -C -Z -p {pid}")
		#os.system(f"strace -xx -y -v -C -p {pid} -o pid_{pid}.log")
