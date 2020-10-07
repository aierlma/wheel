# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:20:47 2020

@author: QGX
"""

import os
a = os.getcwd()
files = os.listdir(a)#取得本目录下所有文件，生成一个列表
print(files)
file1 = open(a+"\\temp.txt","w")



    
for line in files:
    filetype=os.path.splitext(line)[1]
    print(filetype)
    line = "file" + " "+"'"+line+"'"
    print(line)
    if filetype != ".mp4":
        continue
    file1.write(line+"\n")
    
file1.close()

f = open(a+"\\"+"g.txt","w")
f.write("ffmpeg -f concat -i temp.txt -c copy out.mp4")
f.close()
olddir = a+"\\"+"g.txt"
newdir = a+"\\"+"f.bat"
os.rename(olddir,newdir)#重命名