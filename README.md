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