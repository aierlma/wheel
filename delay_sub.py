# -*- coding: utf-8 -*-
"""
Created on Mon May 17 08:13:41 2021

@author: AierlmaQuang
"""
import os
import pysrt

a = os.getcwd()

file = [name for name in os.listdir(os.getcwd()) if
os.path.splitext(name)[1] == '.srt']
file.sort(key = lambda x: int(x[:-4]))        #后面的-4指代文件后缀名
print(file)
for i in range(len(file)):
    
    subs = pysrt.open(file[i])
    subs.shift(minutes=2*i,seconds=58*i)
    subs.save(str(i+1)+'new.srt', encoding='utf-8')