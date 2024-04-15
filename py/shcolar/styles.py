def bold(code):
	return code.replace("[", "[1;");

def italic(code):
	return code.replace("[", "[3;");

def underline(code):
	return code.replace("[", "[4;");

def invert(code):
	return code.replace("[", "[7;");