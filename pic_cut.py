# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:12:23 2020

@author: Aierlma
"""

from PIL import Image
import os
import os.path

#指明被遍历的文件夹
rootdir = os.getcwd()
for parent, dirnames, filenames in os.walk(rootdir):#遍历每一张图片
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the full name of the file is :' + currentPath)
   
        img = Image.open(currentPath)
        
        print (img.format, img.size, img.mode)
        #img.show()
        box1 = (83, 399, 638, 465)#设置左边界、上边界、右边界、下边界的位置坐标像素，通过画图工具得出
        image1 = img.crop(box1) # 图像裁剪
        image1.save(rootdir +'//9'+filename) #存储裁剪得到的图像
        #test
