# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:54:19 2020

@author: QGX
"""


import os
import shutil

a = os.getcwd()
IMAGES_FORMAT = ['.jpg', '.JPG','.jpeg',".JPEG"] # 图片格式
filename = [name for name in os.listdir(a) for item in IMAGES_FORMAT if
os.path.splitext(name)[1] == item]


def delete(i,foo):   #定义删除函数
    x = (i-1)*20-1
    for _ in foo:
        ind = x + _
        os.remove(a + '\\' + filename[ind])

while 1 > 0:
    z = int(input("在第几页"))
    m = input("在第几个，用空格分开")
    try :
        y = list(map(lambda x:int(x),list(m.split(' '))))
        delete(z,y)
    except:
        print('刚刚输错了！')