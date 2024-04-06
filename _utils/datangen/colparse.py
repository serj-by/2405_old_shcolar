#! /usr/bin/env python
import csv, sys

py_path="../../py/shcolar/"
#out_fn_default="__init__.py
out_fn_py_pkg=py_path+"__init__.py"
out_fn_py_fg=py_path+"fg.py"
out_fn_py_bg=py_path+"bg.py"

#settings
esc="\033"
escQ="\\033"
ctrlPfx="["
ctrlSfx="m"

in_fn="_data/shcolar/colors_wiki.txt"
skip_1st_lines_n=4

alls="'reset', 'fg_reset', 'bg_reset'"
py_pkg_header="""
__version__=\'1.0.0\'
__author__=\"Serj.by\"

from . import fg
from . import bg
__all__=['reset', 'fg_reset', 'bg_reset', 'fg', 'bg']

"""

py_pkg_res = """
reset=\"\\033[0m\";
fg_reset=\"\\033[39m\";
bg_reset=\"\\033[49m\";


"""



exec(py_pkg_res)
py_pkg_res=py_pkg_header+py_pkg_res
py_fg_res="";
py_bg_res="";
with open(in_fn) as inf:
	for i in range(skip_1st_lines_n):
	    lines=inf.readline()
	    print ("skip line ",i,":",lines)
	infrdr=csv.reader(inf, delimiter="\t")
	for linear in infrdr:
		#print ("rdrres:", line)
		color=linear[2]
		opidx=color.find("(")
		if opidx!=-1:
			cpidx=color.find(")", opidx)
			color=color[opidx+1:cpidx]
#color2col   orvarname convert
		color=color.replace (" ","")
		color=color[0].lower()+color[1:]
		colVal=int(linear[0])-30
		fgVal=colVal+30
		bgVal=colVal+40
		fgVals,bgVals=str(fgVal),str(bgVal)
		fgVarVals=escQ+ctrlPfx+fgVals+ctrlSfx
		bgVarVals=escQ+ctrlPfx+bgVals+ctrlSfx
		fgVals=esc+ctrlPfx+fgVals+ctrlSfx
		bgVals=esc+ctrlPfx+bgVals+ctrlSfx
		fgVarName=color
		bgVarName=color
		
		#alls +=(", " if alls!="" else "")+"'"+fgVarName+"', "+"'"+bgVarName+"'"
		lineFgs = fgVarName+"=\""+fgVarVals+"\";\n"
		lineBgs = bgVarName+"=\""+bgVarVals+"\";\n"
		print (color, "color found:",fgVals,"FG",fg_reset,bgVals,"BG",bg_reset)
		py_fg_res+=lineFgs
		py_bg_res+=lineBgs
print ("going to write pkg to",out_fn_py_pkg,"\n")
print ("going to write fg module to",out_fn_py_fg,"\n")
print ("going to write bg module to",out_fn_py_bg,"\n")
bw_pkg=bw_fg=bw_bg=-1
with open (out_fn_py_pkg, "w") as outf:
	bw_pkg=outf.write(py_pkg_res)
with open (out_fn_py_fg, "w") as outf:
	bw_fg=outf.write(py_fg_res)
with open (out_fn_py_bg, "w") as outf:
	bw_bg=outf.write(py_bg_res)
print ("Successfully wrote", bw_pkg, "to", out_fn_py_pkg)
print ("Successfully wrote", bw_fg, "to", out_fn_py_fg)
print ("Successfully wrote", bw_bg, "to", out_fn_py_bg)
print ("All done...")
