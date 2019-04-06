===========================================
Git Documentation 
===========================================
Check whether a **directory is linked** with git or not 

	>>> git remote show origin 
	>>> git remote -v
	>>> #result
	>>> origin  https://github.com/Dib-Dey/Dib-Dey.github.io.git (fetch)
	>>> origin  https://github.com/Dib-Dey/Dib-Dey.github.io.git (push) 

If you get error with origin address, remove and add origin again(**first time cloning only**).

	>>> git remote rm origin
	>>> git remote add origin https://github.com/Dib-Dey/Dib-Dey.github.io.git 

check if a directory is **git controlled**:

	>>> git rev-parse --is-inside-work-tree

remove a file from tracking not local untracked file (**not** delete completely)

	>>> git rm --cached calculator_gui/gui.pyc

===========================================
github setup
===========================================
set up github repo for first time

You can follow steps in following web:

	>>> https://pages.github.com/

It will generate git repo. The address:*https://github.com/Dib-Dey/Dib-Dey.github.io.git*.  where sphinx **build** added.

	>>> #go inside the folder c:\deydocuments\coding\build
	>>> git remote add origin https://github.com/Dib-Dey/Dib-Dey.github.io.git

Sphinx help for GitHub can be found in `Sphinx help <https://daler.github.io/sphinxdoc-test/includeme.html>`_
If you getting a 404 error, try the following:
	
	>>> cd <location of build> #example - C:\deydocuments\coding\build
	>>> touch .noj\ekyll
	>>> git add .nojekyll
	>>> git commit -m "added .nojekyll"