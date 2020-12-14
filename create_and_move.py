# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:33:10 2020

@author: Aierlma
"""

import os
import shutil

a = os.getcwd()
FORMAT = ['.avi','.mp4',".mkv"] # 要依据的格式
file_names = [name for name in os.listdir(a) for item in FORMAT if os.path.splitext(name)[1] == item]
for file in file_names:
    Olddir=os.path.join(a,file)   #原来的文件路径
    if os.path.isdir(Olddir):   #如果是文件夹则跳过
        continue
    filename=os.path.splitext(file)[0]   #文件名
    print (filename)
    os.mkdir(a+'\\'+filename)
    shutil.move(Olddir, a+'\\'+filename)
