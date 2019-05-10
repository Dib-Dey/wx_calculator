===========================================
Python few useful BKMs 
===========================================
to do when module isn't recognized. Path to be added to sys

	> Python
	>>> import sys
	>>> sys.path.append(r"C:\deydocuments\coding")
	>>># one can import any module inside the directory as above 
	>>> import pypo

auto-completion using Tab, need to add following lines in __init__

	>>> import rlcompleter, readline
	>>> readline.parse_and_bind('tab:complete')

How to check if a package is installed or not?

	>>> pip show py2exe
	>>> # example above shows about the package 