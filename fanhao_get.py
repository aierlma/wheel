# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:32:04 2021

@author: AierlmaQuang
"""
import requests
import os
import re

x = os.getcwd()
c = ['https://www.dmmbus.blog/search/%E6%9E%97%E3%82%86%E3%81%AA','https://www.dmmbus.blog/search/%E6%9E%97%E3%82%86%E3%81%AA/2']  #查找的网页
with open(x+'//result.txt',"w") as f:
    
    for i in c:
        a = requests.get(i) 
        b = a.text
        #print(b)
        
        
        t = re.findall(r'[A-Za-z]{2,5}-[0-9]{3}',b,flags=0)
          
        t = list(set(t))
        print(t)
        for i in t:
            f.write(i+',')