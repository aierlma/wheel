# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:58:15 2021

@author: AierlmaQuang
"""
import re
with open('a.txt','r',encoding='utf-8') as f:

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
        with open('b.txt','a+',encoding='utf-8') as fl:
            fl.write(line)            