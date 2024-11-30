SelectPlus for Sublime Text 2 and 3
===================================
Advanced selection management for Sublime Text.

This is a plugin for [Sublime Text 2](http://www.sublimetext.com/2) and [Sublime Text 3](http://www.sublimetext.com/3). It provides advanced selection management features, including:
- Extending selections to the left or right using keyboard shortcuts.
- Saving, restoring, adding, subtracting, and exchanging selections.

Installation
------------

I hope soon it will be possible to use Package Control to install `SelectPlus`

For the moment:

1. Open the Sublime Text Packages folder

  - for ST2
    - macOS: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/
  - for ST3
    - macOS: ~/Library/Application Support/Sublime Text 3/Data/Packages/
    - Windows: %programfiles%/Sublime Text 3/Data/Packages/
    - Linux: ~/.Sublime Text 3/Data/Packages/

2. clone this repo (`git clone git://github.com/kpym/SublimeSelectPlus SelectPlus`).

How to use
----------
* You can use `ctrl+left` and `ctrl+right` to set the "end" to the left or right **border** of the selection. Then, y
* You can use `sift+left` and `shift+right` to move the "end" border.
* You can use `alt+left` and `alt+right` to **move selection**.
* To **save selection**: `alt+s`, `s`
* To **restore selection**: `alt+s`, `=`
* To **add selection**: `alt+s`, `+`
* To **subtract selection**: `alt+s`, `-`
* To **exchange selection**: `alt+s`, `x`
* To **inverse selection**: `alt+s`, `!`
* To **extend selection to**: 
  * `alt+s`, `t` for literal ignore case search
  * `alt+s`, `T` for literal case sensitive search
  * `alt+s`, `r` for regex ignore case search
  * `alt+s`, `R` for regex case sensitive search
* To **select to bookmark**: 
  * `alt+shift+left` to select to the previous bookmark (if any)
  * `alt+shift+right` to select to the next bookmark (if any)


Commands
--------
See [Default.sublime-keymap](Default.sublime-keymap) in this folder

BUG
---
There is a bug in the Sublime Text 2 and 3 API `regions.subtract`:
If a < b < c, when we subtract the region [a,b] from the region [a,c] the result is [a,a] and not the expected [b,c].
So in some situations **subtract selection** is not working properly.

LICENSE
-------
This plugin is released under the MIT license. See [LICENSE](LICENSE) for details.