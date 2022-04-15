# -*- coding: utf-8 -*-
"""
Created on Mon May 17 08:32:21 2021

@author: AierlmaQuang
"""
import os 
import pysrt

file = [name for name in os.listdir(os.getcwd()) if os.path.splitext(name)[1] == '.srt']
file.sort(key = lambda x: int(x[:-7])) 
print(file)
sub = pysrt.open(file[0])
with open('all.txt','w') as f:
    for i in range(len(file)):
        sub = pysrt.open(file[i])
        for line in sub:
            f.write(str(line))
            f.write('\n')