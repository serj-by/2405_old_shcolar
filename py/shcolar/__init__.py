
__version__='1.0.0'
__author__="Serj.by"

from . import fg
from . import bg
__all__=['reset', 'fg_reset', 'bg_reset', 'fg', 'bg', 'fg.green', 'bg.brightBlue']


reset="\033[0m";
fg_reset="\033[39m";
bg_reset="\033[49m";

default="\033[m";


def bold(basecode):
	return basecode.replace("[", "[1;");

def italic(basecode):
	return basecode.replace("[", "[3;");

def underline(basecode):
	return basecode.replace("[", "[4;");


def blink(basecode):
	return basecode.replace("[", "[5;");
	
def inverse(basecode):
	return basecode.replace("[", "[7;");

def strike(basecode):
	return basecode.replace("[", "[9;");
