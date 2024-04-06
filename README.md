SHColar stands for **SHell COLors**

It is Python (and PHP in future versions)  library providing strings representing ANSI escape codes for coloring output for most modern terminals.

Color escape codes are from [Wikipedia](https://en.m.wikipedia.org/wiki/ANSI_escape_code) (Description>Colors>3-bit and 4-bit)

Usage examples:

Create bold green text:

`print (shcolar.bold(shcolar.fg.green)+"Bold green text"+shcolar.reset)`

Create bold text with default color:

`print (shcolar.bold(shcolar.default)+"Bold default color text"+shcolar.reset)`

Create italic text with default color:

`print (shcolar.italic(shcolar.default)+"Italic default color text"+shcolar.reset)`

Create underlined text with default color:

`print (shcolar.underline(shcolar.default)+"Underlined default color text"+shcolar.reset)`

Also you can combine all of the attributes above. E.g. green bold underlined text:

`print (shcolar.underline(shcolar.bold((shcolar.fg.green)))+"Bold underlined green text"+shcolar.reset)`

You could even use your own SGR attribute code to use in your escape sequence (e.g. this one is similar to bold function (ANSI code 1). However it could be used for any unsupported (SGR)[https://en.m.wikipedia.org/wiki/Select_Graphic_Rendition_(ANSI)] parameter:

`print (shcolar.customattr(shcolar.fg.green, 1)+"Bold Green using customattr"+shcolar.reset)`

_lplease note that you should append `shcolar.reset` at the end of string to make terminal return to default color/text decoration values. However you may not if you wish to left with your settings in terminal after print finished._