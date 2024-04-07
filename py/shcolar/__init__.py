
__version__='1.0.0'
__author__="Serj.by"

from . import fg
from . import bg
__all__=['esc', 'colots_n', 'ctrl_sfx', 'ctrl_pfx', 'reset', 'fg_reset', 'bg_reset', 'fg', 'bg']


reset="\033[0m";
fg_reset="\033[39m";
bg_reset="\033[49m";

esc="\033";
ctrl_pfx=esc+"[";
ctrl_sfx="m"
colors_n=8

def bold(col):
	return col.replace("[", "[1;");

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
