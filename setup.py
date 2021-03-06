#!/usr/bin/env python

from distutils.core import setup

setup(name='Automagica',
      version='0.3',
      description='Bot for Automagica - Smart Robotic Process Automation',
      author='Koen van Eijk',
      author_email='koen@oakwood.ai',
      url='https://oakwood.ai/',
      entry_points = {
        'console_scripts': ['automagica=automagica.command_line:main'],
      },
      packages=['automagica'],
      package_data={'automagica':[
        'bin/win32/chromedriver.exe',
        'bin/mac64/chromedriver',
        'bin/linux64/chromedriver']},
      install_requires=[
          'socketIO-client==0.7.2',
          'PyAutoGUI==0.9.36',
          'opencv-python==3.4.0.12',
          'sty==1.0.0b2',
          'selenium==3.7.0',
          'pywinauto==0.6.1',
          'pytesseract==0.2.0',
          'openpyxl==2.4.8',
          'python-docx==0.8.6',
          'pywin32==223'
      ],
      include_package_data = True
)