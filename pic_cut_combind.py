# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:54:19 2020

@author: QGX
"""

import PIL.Image as Image
import os
import os.path
import shutil


rootdir = os.getcwd()
os.mkdir(rootdir+'\\'+'new')
a = int(input("左边界坐标"))
b = int(input("上边界坐标"))
c = int(input("右边界坐标"))
d = int(input("下边界坐标"))
Total = int(input('一共要合并多少张'))   #一共要合并多少张
for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    for filename in filenames:
        try:
            #print('parent is :' + parent)
            #print('filename is :' + filename)
            currentPath = os.path.join(parent, filename)
            #print('the full name of the file is :' + currentPath)

            img = Image.open(currentPath)

            print(img.format, img.size, img.mode)
            #img.show()
            box1 = (a, b, c, d)  # 设置左边界、上边界、右边界、下边界的位置坐标像素，通过画图工具得出
            image1 = img.crop(box1)  # 图像裁剪
            image1.save(rootdir + '//9'+filename)  # 存储裁剪得到的图像
            shutil.move(currentPath, rootdir+'\\'+"new")
        except:
            pass

IMAGES_PATH = os.getcwd() # 图片集地址
print(IMAGES_PATH)
IMAGES_FORMAT = ['.jpg', '.JPG','.jpeg',".JPEG"] # 图片格式
IMAGE_SIZE1 = d-b # 每张小图片的纵高
IMAGE_SIZE2 = c-a #每张小图片的横长
IMAGE_ROW = 20 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1 # 图片间隔，也就是合并成一张图后，一共有几列

circulation = Total //IMAGE_ROW


# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
os.path.splitext(name)[1] == item]

# 定义图像拼接函数
def image_compose(foo,_):
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE2, IMAGE_ROW * IMAGE_SIZE1)) #创建一个新图
# 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + "\\" + image_names[IMAGE_COLUMN * (y - 1) + x - 1+foo])
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE2, (y - 1) * IMAGE_SIZE1))
    a = str(_)
    s = a.zfill(4)
    return to_image.save("0final"+s+".jpeg") # 保存新图

for i in range(circulation):                 #要循环几次
    foo = i*IMAGE_ROW
    image_compose(foo,i)#调用函数
