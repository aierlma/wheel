# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:25:35 2020

@author: Aierlma
"""

import requests
import os
import re

Videos_FORMAT = ['.mp4', '.MP4','.mkv',".avi"] # 视频格式
vidslst1 = []

for root, dirs, files in os.walk(os.getcwd()):          #游走文件夹，获得所有文件，不仅一层子文件夹
    for i in files:
        filetype = os.path.splitext(i)[1]
        if filetype in Videos_FORMAT:
            filename = os.path.splitext(i)[0]
            directory = os.path.join(root,i)
            
            vidslst1.append(directory)

sub_FORMAT = ['.srt', '.ass','.ssa',".vtt",'smi']
sublst = []
for i in vidslst1:

    filename = os.path.basename(i)
    fanhao = os.path.splitext(filename)[0]
    path = os.path.dirname(i)
    files = os.listdir(path)
    for fl in files:
        for typ in sub_FORMAT:
            if fl.endswith(typ):
                sublst.append(fl)
print(sublst)
count = 0
with open('sub.txt','w') as f:
    for i in vidslst1:
        if '-C' in i or '-c' in i:
            continue
        if "[" in i:
            i = re.sub('\\[.*?\\]', '', i)
        filename = os.path.basename(i)
        fanhao = os.path.splitext(filename)[0]
        path = os.path.dirname(i)
        files = os.listdir(path)

        
        if any(fanhao in sub.lower() for sub in sublst):
            
            continue
        print(fanhao)
        c = 'https://www.dmmbus.blog/%s'%fanhao
        a = requests.get(c) 
        print(c)
        b = a.text
        print("包含字幕的磁力連結" in b)
        if "包含字幕的磁力連結" in b:
            count += 1
            f.write('https://www.dmmbus.blog/%s'%fanhao + "\n")
        
        
print(count)