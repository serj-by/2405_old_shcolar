'''
Module contains functions to stylize text in terminals. Most function accept colorizing escape-sequence as parameter. Use shcolar.empty escape-sequence to stay with your  current colors
'''
def bold(code):
	'''
	Make all following text bold
	'''
	return code.replace("[", "[1;");

def italic(code):
	return code.replace("[", "[3;");

def underline(code):
	return code.replace("[", "[4;");

def invert(code):
	return code.replace("[", "[7;");