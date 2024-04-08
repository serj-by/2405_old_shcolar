#! /usr/bin/env python
s="""
test "dblquot"
test 'snglquot'
// single line comment
/*
multi line comment
second line with 'single' & "double" quotes
*/
"""

print (s)
with open("quotetest.txt", "w") as outf:
	bw=outf.write(s)
	print ("Bytes wrote:", bw)