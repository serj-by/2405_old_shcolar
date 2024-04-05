#! /usr/bin/env python
import csv, sys

#out_fn_default="__init__.py
out_fn_pkg="__init__.py"
out_fn_fg="fg.py"
out_fn_bg="bg.py"

#settings
esc="\033"
escQ="\\033"
ctrlPfx="["
ctrlSfx="m"

in_fn="_info/colors_wiki.txt"
skip_1st_lines_n=4

alls="'shcol_reset', 'shcol_fg_reset', ' shcol_bg_reset'"
pkg_header="""
__version__=\'1.0.0\'
__author__=\"Serj.by\"

from . import fg
from . import bg
__all__=['shcolar_reset', 'shcolar_fg_reset', 'shcolar_bg_reset', 'fg', 'bg']

"""

res = """
shcolar_reset=\"\\033[0m\";
shcolar_fg_reset=\"\\033[39m\";
shcolar_bg_reset=\"\\033[49m\";


"""



exec(res)
pkg_res=pkg_header+res
fg_res="";
bg_res="";
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
		print (color, "color found:",fgVals,"FG",shcolar_fg_reset,bgVals,"BG",shcolar_bg_reset)
		print(lines)
		fg_res+=lineFgs
		bg_res+=lineBgs
print ("pkg tes:\n",pkg_res)
print ("going to write pkg to",out_fn_pkg,"\n")
print ("going to write fg mofule to",out_fn_fg,"\n")
print ("going to write bg mofule to",out_fn_bg,"\n")
bw_pkg=bw_fg=bw_bg=-1
with open (out_fn_pkg, "w") as outf:
	bw_pkg=outf.write(pkg_res)
with open (out_fn_fg, "w") as outf:
	bw_fg=outf.write(fg_res)
with open (out_fn_bg, "w") as outf:
	bw_bg=outf.write(bg_res)
print ("Successfully wrote", bw_pkg, "to", out_fn_pkg)
print ("Successfully wrote", bw_fg, "to", out_fn_fg)
print ("Successfully wrote", bw_bg, "to", out_fn_bg)
print ("All done...")
