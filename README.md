SelectPlus for Sublime Text 2
===============================
This is a plugin for [Sublime Text 2](http://www.sublimetext.com/2).
This plugin add some features to manage selections :

- possibility to extend selections on the right and on the left using keyboard only 
- possibility to save/restore/add/subtract/exchange selections


Installation
------------

I hope soon it will be possible tu use Package Control to install `SelectPlus`

For the moment:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo

How to use
----------
* You can use `ctrl+left` and `ctrl+right` **to move to** the left or right **border** of the selection. Then, you can use `sift+left` and `shift+right` to modify this selection border.
* You can use `alt+left` and `alt+right` to **move selection**.
* To **save selection** : `alt+s`, `s`
* To **reststore selection** : `alt+s`, `=`
* To **add selection** : `alt+s`, `+`
* To **subtract selection** : `alt+s`, `-`
* To **exchange selection** : `alt+s`, `x`


Commands
--------
See Default.sublime-keymap in this folder