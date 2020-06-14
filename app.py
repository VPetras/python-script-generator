#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Python script generator
# Title: This is python script which creates directory with app.py and includes automatically header.
# Author: Vojtěch Petrásek
# Generated: 14/06/2020 16:26:21
##################################################

from datetime import datetime
import os

now = datetime.now()

dirName = input('Type name of project: ')

title = input('Enter a simple description of the project: ')

while True:
    pythonVersion = input ('Do you want use: A) Python3. B) Python2.7. [A/B]? : ')
    if pythonVersion in ['A', 'B']:
        break

if pythonVersion == 'A':
    pythonVersion = 'python3'
elif pythonVersion == 'B':
    pythonVersion = 'python'


# Create target Directory if don't exist
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")

app = open('{0}/app.py'.format(dirName),'w+')

app.write('#!/usr/bin/env {0}\n'.format(pythonVersion))
app.write('# -*- coding: utf-8 -*-\n\n')
app.write(50*'#'+'\n')
app.write('# {0}\n'.format(dirName))
app.write('# Title: {0}\n'.format(title))
app.write('# Author: Vojtěch Petrásek \n')
app.write('# Generated: {0}\n'.format(now.strftime("%d/%m/%Y %H:%M:%S")))
app.write(50*'#'+'\n')
app.close()
