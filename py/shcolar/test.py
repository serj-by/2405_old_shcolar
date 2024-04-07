#! /usr/bin/env python
import shcolar
def test_pkg(attr_n):
	print ("Test table with additional attribute", str(attr_n))
	for r in range(-1, shcolar.colors_n):
		if r==-1:
			print(shcolar.bg.white+shcolar.fg.black)
		for c in range(shcolar.colors_n):
			ctrl_vals=str(attr_n)+";"+str(30+c)+";"+str(40+r)
			vals=" "+str(c)+("-" if r==-1 else str(r))+" "
			print (shcolar.ctrl_pfx+ctrl_vals+shcolar.ctrl_sfx+vals+shcolar.reset, end=("" if c<7 else "\n"))
		if r==-1:
			print("FG"+shcolar.reset)

if __name__=="__main__":
	print ("Test Colors tables")
	for at in range(10):
		test_pkg(at);