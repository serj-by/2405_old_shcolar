#! /usr/bin/env python
import shcolar
def test_pkg():
                for r in range(8):
                        for c in range(8):
                                ctrl_vals=str(30+c)+";"+str(40+r)
                                vals=" "+str(c)+str(r)+" "
                                print (shcolar.ctrl_pfx+ctrl_vals+shcolar.ctrl_sfx+vals+shcolar.reset, end=("" if c!=7 else "\n"))

if __name__=="__main__":
	print ("Test colors table")
	test_pkg();