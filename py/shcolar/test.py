#! /usr/bin/env python
import shcolar
def test_pkg(attr_n):
	print ("Table with additional attribute", str(attr_n))
	for r in range(8):
		for c in range(8):
			ctrl_vals=str(attr_n)+";"+str(30+c)+";"+str(40+r)
			vals=" "+str(c)+str(r)+" "
			print (shcolar.ctrl_pfx+ctrl_vals+shcolar.ctrl_sfx+vals+shcolar.reset, end=("" if c!=7 else "\n"))

if __name__=="__main__":
	print ("Test Colors tables")
	for at in range(10):
		test_pkg(at);