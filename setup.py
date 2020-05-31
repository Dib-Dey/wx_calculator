# -*- coding: UTF-8 -*-
import sys
import os
from setuptools import setup
from setuptools import find_packages

######################
toolname = "Wx_CalC"
package_name = "CalC.Wx_CalC"
######################

__version__ = "1.0.0"

# build package_dir first
package_list = find_packages()

setup(name=package_name,
      version=__version__,
      description = "Calculator GUI based on wx.python" ,
      author='Dibyendu Dey',
      author_email='',
      packages=package_list,
      install_requires=[
            'wxPython'
            ],
      entry_points={
            'console_scripts': [
                    'Wx_CalC = CalC.__main__:main',
            ],
      },
     )