
__version__='1.0.0'
__author__="Serj.by"

from . import fg
from . import bg
__all__=['shcolar_reset', 'shcolar_fg_reset', 'shcolar_bg_reset', 'fg', 'bg']


shcolar_reset="\033[0m";
shcolar_fg_reset="\033[39m";
shcolar_bg_reset="\033[49m";


