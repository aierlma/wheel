# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:58:15 2021

@author: AierlmaQuang
"""
import re
import os
files = [i for i in os.listdir(os.getcwd()) if i.endswith('.ass')]
lst = []
for _ in files:
    llst = []
    with open(_,'r',encoding='utf-8') as f:
    
        for line in f:
            if 'move' in line:
                p1 = re.compile(r'[(](.*?)[)]')
                res = p1.search(line)
                rs = res.group()
                tp = str(rs)
                lst = tp.split(',')
                num = int(lst[1])
                
                if num>120:
                    continue
            llst.append(line)
            
            
    os.remove(_)
    for foo in llst:
        with open(_,'a+',encoding='utf-8') as fl:
            fl.write(foo)            
