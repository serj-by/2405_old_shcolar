# SHColar stands for **SHell COLors**

It is Python (and PHP in future versions)  library providing strings representing ANSI escape codes for coloring output for most modern terminals.

Color escape codes are from [Wikipedia](https://en.m.wikipedia.org/wiki/ANSI_escape_code) (Description>Colors>3-bit and 4-bit)

## Tested in:
### Android Termux
`
## Termux App Info

**APP_NAME**: `Termux`  
**PACKAGE_NAME**: `com.termux`  
**VERSION_NAME**: `0.118.0`  
**VERSION_CODE**: `118`  
**TARGET_SDK**: `28`  
**IS_DEBUGGABLE_BUILD**: `false`  
**APK_RELEASE**: `F-Droid`  
**SIGNING_CERTIFICATE_SHA256_DIGEST**: `228FB2CFE90831C1499EC3CCAF61E96E8E1CE70766B9474672CE427334D41C42`  
##


## Termux:API App Info

**APP_NAME**: `Termux:API`  
**PACKAGE_NAME**: `com.termux.api`  
**VERSION_NAME**: `0.50.1`  
**VERSION_CODE**: `51`  
**TARGET_SDK**: `28`  
**IS_DEBUGGABLE_BUILD**: `false`  
**APK_RELEASE**: `F-Droid`  
**SIGNING_CERTIFICATE_SHA256_DIGEST**: `228FB2CFE90831C1499EC3CCAF61E96E8E1CE70766B9474672CE427334D41C42`  
##


## Device Info

### Software

**OS_VERSION**: `4.14.116`  
**SDK_INT**: `29`  
**RELEASE**: `10`  
**ID**: `HONORSTK-LX1`  
**DISPLAY**: `STK-L21VHN 10.0.0.233(C185E2R4P1)`  
**INCREMENTAL**: `10.0.0.233C185`  
**SECURITY_PATCH**: `2020-08-01`  
**IS_DEBUGGABLE**: `0`  
**IS_TREBLE_ENABLED**: `true`  
**TYPE**: `user`  
**TAGS**: `release-keys`  

### Hardware

**MANUFACTURER**: `HUAWEI`  
**BRAND**: `HONOR`  
**MODEL**: `STK-LX1`  
**PRODUCT**: `STK-L21VHN`  
**BOARD**: `STK-L21VHN`  
**HARDWARE**: `kirin710`  
**DEVICE**: `HWSTK-HF`  
**SUPPORTED_ABIS**: `arm64-v8a, armeabi-v7a, armeabi`  
##

bash --version


GNU bash, version 5.2.26(1)-release (aarch64-unknown-linux-android)
`

## Usage examples:

### Python

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

You could even use your own SGR attribute (link to desription see below) code to use in your escape sequence (e.g. this one is similar to bold function (ANSI code 1). However it could be used for any unsupported [SGR](https://en.m.wikipedia.org/wiki/Select_Graphic_Rendition_%28ANSI%29) parameter:

`print (shcolar.customattr(shcolar.fg.green, 1)+"Bold Green using customattr"+shcolar.reset)`

Please note that you should append `shcolar.reset` at the end of string to make terminal return to default color/text decoration values. However you may not if you wish to left with your settings in terminal after print finished._
