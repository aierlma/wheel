# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:32:13 2021

@author: AierlmaQuang
"""
import os 
import re
import shutil
Videos_FORMAT = ['.mp4', '.MP4','.mkv',".avi"] # 图片格式
vidslst1 = []

for root, dirs, files in os.walk(os.getcwd()):          #游走文件夹，获得所有文件，不仅一层子文件夹
    for i in files:
        filetype = os.path.splitext(i)[1]
        if filetype in Videos_FORMAT:
            filename = os.path.splitext(i)[0]
            directory = os.path.join(root,i)
            
            vidslst1.append(directory)


sublst = []
sub_FORMAT = ['.srt', '.ass','.ssa',".vtt",'smi'] # 图片格式
sublst = [name for name in os.listdir('F:\OneDrive - aierlmalee\MC\sub\AVsub') for item in sub_FORMAT if
os.path.splitext(name)[1] == item]                                      #获取字幕文件形成列表



for i in vidslst1:
    newpath = os.path.dirname(i)
   
    file = os.path.basename(i)
    filename = os.path.splitext(file)[0]

    try:
        fanhao = re.search(r'[A-Za-z]{2,5}-[0-9]{3}',filename,flags=0).group()  #尝试正则匹配番号，意思是匹配大小写字母2到5次，再匹配短横杠-再匹配数字3次
    except:
        continue


    for j in sublst:
        if str(fanhao) in str(j):
            oldpath = 'F:\\OneDrive - aierlmalee\\MC\\sub\\AVsub'+'\\'+str(j)
            print(oldpath,newpath)
            shutil.copy(oldpath,newpath)
            print("finish1")

