#!/usr/bin/python

import os,re,sys,commands

def main(argv):
	oql=" ".join(argv)

	if not oql.startswith("select"):
		oql = "select s from instanceof %s s" % oql
	oql = oql.replace(" ", "+")
	status, output = commands.getstatusoutput("wget -O - http://localhost:7000/oql/?query="+oql+" | grep '/object/'")
	if output:
		print output

	return status and 1 or 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))