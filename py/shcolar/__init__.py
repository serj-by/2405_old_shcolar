
__version__='1.0.0'
__author__="Serj.by"

from . import fg
from . import bg
__all__=['ctrl_sfx', 'ctrl_pfx', 'reset', 'fg_reset', 'bg_reset', 'fg', 'bg']


reset="\033[0m";
fg_reset="\033[39m";
bg_reset="\033[49m";

ctrl_pfx="\033["
ctrl_sfx="m"


def bold(col):
	return col.replace("[", "[1;");
9
def italic(col):
	return col.replace("[", "[3;");

def underline(col):
	return col.replace("[", "[4;");

def blink(col):
	return col.replace("[", "[6;");

def invert(col):
	return col.replace("[", "[7;");

def customattr(col, attrn):
	return  col.replace("[", "["+str(attrn)+";");
	
	def test_plg():
		for r in range(8):
			for c in range(8):
				ctrl_vals=str(30+c)+";"+str(40+r)
				vals=str(c)+str(r)
				print (ctrl_pfx+ctrl_valss+ctrl_sfx+vals+reset)
	
	if __name=="__main__":
		print ("Test colors table")
		test_pkg();