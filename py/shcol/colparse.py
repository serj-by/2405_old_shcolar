#! /usr/bin/env python
import csv, sys

out_fn_default="__init__.py"


#settings
fgVarPfx="shcol_fg_"
bgVarPfx="shcol_bg_"
esc="\033"
escQ="\\033"
ctrlPfx="["
ctrlSfx="m"
allTag="\"<@all>\""

in_fn="_info/colors_wiki.txt"
skip_1st_lines_n=4

alls="'shcol_reset', 'shcol_fg_reset', ' shcol_bg_reset'"

module_header="""
__version__=\'1.0.0\'
__author__=\"Serj.by\"
__all__=[\"<@all>\"]

"""

res = """
shcol_reset=\"\\033[0m\";
shcol_fg_reset=\"\\033[39m\";
shcol_bg_reset=\"\\033[49m\";

"""
exec(res)
res=module_header+res
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
#color2colorvarname convert
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
		fgVarName=fgVarPfx+color
		bgVarName=bgVarPfx+color
		alls +=(", " if alls!="" else "")+"'"+fgVarName+"', "+"'"+bgVarName+"'"
		lines = fgVarName+"=\""+fgVarVals+"\";\n"
		lines += bgVarName+"=\""+bgVarVals+"\";\n"		
		print (color, "color found:",fgVals,"FG",shcol_fg_reset,bgVals,"BG",shcol_reset)
		print(lines)
		res+=lines
out_fn=out_fn_default
res=res.replace (allTag, alls)
if len(sys.argv)==2:
	out_fn=sys.argv[1]
print (res)
print ("going to write to",out_fn,"\n")
bw=-1
with open (out_fn, "w") as outf:
	bw=outf.write(res)
print ("Successfully wrote", bw, "to", out_fn)	
print (__name__)
