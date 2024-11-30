SelectPlus for Sublime Text 2 and 3
===================================
This is a plugin for [Sublime Text 2](http://www.sublimetext.com/2) and [Sublime Text 3](http://www.sublimetext.com/3).
This plugin add some features to manage selections :

- possibility to extend selections on the right and on the left using keyboard only
- possibility to save/restore/add/subtract/exchange selections


Installation
------------

I hope soon it will be possible tu use Package Control to install `SelectPlus`

For the moment:

1. Open the Sublime Text Packages folder

  - for ST2
    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/
  - for ST3
    - OS X: ~/Library/Application Support/Sublime Text 3/Data/Packages/
    - Windows: %programfiles%/Sublime Text 3/Data/Packages/
    - Linux: ~/.Sublime Text 3/Data/Packages/

2. clone this repo (`git clone git://github.com/kpym/SublimeSelectPlus SelectPlus`).

How to use
----------
* You can use `ctrl+left` and `ctrl+right` **to move to** the left or right **border** of the selection. Then, you can use `sift+left` and `shift+right` to modify this selection border.
* You can use `alt+left` and `alt+right` to **move selection**.
* To **save selection** : `alt+s`, `s`
* To **reststore selection** : `alt+s`, `=`
* To **add selection** : `alt+s`, `+`
* To **subtract selection** : `alt+s`, `-`
* To **exchange selection** : `alt+s`, `x`
* To **inverse selection** : `alt+s`, `!`
* To **extend selection to** : 
  * `alt+s`, `t` for literal ignore case search
  * `alt+s`, `T` for literal case sensitive search
  * `alt+s`, `r` for regex ignore case search
  * `alt+s`, `R` for regex case sensitive search


Commands
--------
See Default.sublime-keymap in this folder

BUG
---
There is a bug in the Sublime Text 2 and 3 API `regions.subtract`:
If a < b < c, when we subtract the region [a,b] from the region [a,c] the result is [a,a] and not the expected [b,c].
So in some situations **subtract selection** is ont working properly.
