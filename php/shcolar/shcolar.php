<?php
namespace serj_by\shcolar;

class shcolar {
const esc="\033";
const ctrlPfx="[";
const ctrlSfx="m";
class fg {
const green=parent::esc."32".parent::ctrlSfx;
}
/*
include(__DIR__."fg.php");
include(__DIR__."bg.php");
*/
}

var_dump (shcolar:fg);

?>