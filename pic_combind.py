# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:54:19 2020

@author: Aierlma
"""

import PIL.Image as Image
import os
import shutil
IMAGES_PATH = os.getcwd() # 图片集地址
print(IMAGES_PATH)
IMAGES_FORMAT = ['.jpg', '.JPG','.jpeg',".JPEG"] # 图片格式
IMAGE_SIZE1 = 480 # 每张小图片的纵高
IMAGE_SIZE2 = int#每张小图片的横长
IMAGE_ROW = 20 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1 # 图片间隔，也就是合并成一张图后，一共有几列

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
os.path.splitext(name)[1] == item]
Total =   len(image_names)   #一共要合并多少张
circulation = Total //IMAGE_ROW
rest = Total %IMAGE_ROW
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
os.mkdir(IMAGES_PATH+'//'+'new')
for i in range(circulation):                 #要循环几次
    foo = i*IMAGE_ROW
    image_compose(foo,i)#调用函数
    shutil.move(IMAGES_PATH+'//'+'0final%s.jpeg'%(str(i).zfill(4)),IMAGES_PATH+'//'+'new')#占位符的使用
    print('have moved')
num = circulation*IMAGE_ROW
IMAGE_ROW = rest
numb = circulation
image_compose(num,numb)
shutil.move(IMAGES_PATH+'//'+'0final%s.jpeg'%(str(numb).zfill(4)),IMAGES_PATH+'//'+'new')
print('have moved')
print("finished")
