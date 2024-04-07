#! /usr/bin/env python
s="""
test "dblquot"
test 'snglquot'
"""

print (s)
with open("quotetrst.txt", "w") as outf:
	bw=outf.write(s)
	print ("Bytes wrote:", bw)