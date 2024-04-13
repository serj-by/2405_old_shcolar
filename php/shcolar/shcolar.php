#! /usr/bin/env php
<?php

include(__DIR__."/fg.php");
include(__DIR__."/bg.php");

class shcolar {
const esc="\033";
const ctrlPfx="[";
const ctrlSfx="m";
use shcolar_fg;

}

var_dump (shcolar);

?>