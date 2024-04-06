
__version__='1.0.0'
__author__="Serj.by"

from . import fg
from . import bg
__all__=['reset', 'fg_reset', 'bg_reset', 'fg', 'bg', 'fg.green', 'bg.brightBlue']


reset="\033[0m";
fg_reset="\033[39m";
bg_reset="\033[49m";


