<?php

class shcolar {
static const esc="\033";
static const ctrlPfx="[";
static const ctrlSfx="m";
include(__DIR__."fg.php");
include(__DIR__."bg.php");
}

var_dump (shcolar:fg);

?>