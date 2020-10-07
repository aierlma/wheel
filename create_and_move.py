# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:33:10 2020

@author: QGX
"""

import os
import shutil

a = os.getcwd()
path = a 
filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
for file in filelist:
    if file == "1.TXT" or file == 'a.bat' or file == 'create_and_move.py':
        continue
    Olddir=os.path.join(path,file)   #原来的文件路径
    if os.path.isdir(Olddir):   #如果是文件夹则跳过
        continue
    filename=os.path.splitext(file)[0]   #文件名
    print (filename)
    os.mkdir(a+'\\'+filename)
    
    shutil.move(Olddir, a+'\\'+filename)