#!/usr/bin/python

import os,re,sys,commands,subprocess,shlex,time,oql

def jhat_ready():
	status, output = commands.getstatusoutput("wget -o - http://localhost:7000")
	return status == 0

jhat = subprocess.Popen(shlex.split("jhat -port 7000 " + sys.argv[1]))

while not jhat_ready():
	print "wait for jhat"
	time.sleep(3)

status = oql.main(sys.argv[2:])

jhat.kill()

jhat.wait()

sys.exit(status)