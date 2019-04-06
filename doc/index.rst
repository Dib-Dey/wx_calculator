===========================================
Dey's Coding Documentation 
===========================================

Sphinx doc is created to track all solved problem and its potential use for future references. 

===========================================
Sphinx BKM
===========================================

Get to following directory and run the command as shown below:	

	>>> c:\deydocuments\coding
	>>> sphinx-build -b html C:\deydocuments\coding\doc .\build

add the module for docu in code.rst file. 

	>>> automodule:: Python_problems.minion_game

If you want to show docstring of individual function 

	>>> need to add :members: as shown in code.rst 

Need to change the html theme: `weblink <http://www.sphinx-doc.org/en/stable/theming.html>`_

	>>> go to conf.py
	>>> change the theme variable html_theme = 'classic'

Any good example of docstring manipulation:

	>>> https://pythonhosted.org/an_example_pypi_project/sphinx.html

===========================================
Python Helps
===========================================
.. toctree::
   :maxdepth: 2

   tips.rst

===========================================
Software helps	  
===========================================
.. toctree::
   :maxdepth: 2

   git.rst

===========================================
Software Projects	  
===========================================
.. toctree::
   :maxdepth: 2

   project.rst

===========================================
Solved Problem Statements  
===========================================
.. toctree::
   :maxdepth: 2
   
   code.rst

===========================================
Release Methods   
===========================================
Below are steps to push the Sphinx documentations:	
	* go indisde following directory ``c:\deydocuments\coding\build``
	* ``>git pull``
	* After making new build, Please git add all files: ``git add *``
	* ``git commit -m "put your comments"``
	* ``git push``
	* if have issue with pushing , get out of ``Intel work vnc connection and try``
	* once update is completed check `www.dib-dey.github.io <https://dib-dey.github.io/>`_   

Below are the steps to save the codes:
	* code files need to be copied and move to ``C:\deydocuments\github\Python``
