# -*- coding: utf-8 -*-
'''
Created on 2022/4/15 17:43

'''
import os
path = r'D:\Project\save'
file = os.listdir(path)
print(file)
with open("combind.txt",'w',encoding='utf-8') as f:
    for i in range(len(file)):
        with open(os.path.join(path,file[i]),'r',encoding='utf-8') as t:
            for line in t:
                f.write(line+'\n')