# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:11:07 2020

@author: AierlmaQuang
"""
import os
import codecs
import chardet


#检验文本文件的编码格式并转为utf-8

def gbk_2_utf8(filename,out_enc="UTF-8"):
    try:
        content = open(filename, 'rb').read()
        source_encoding = chardet.detect(content)
        print("编码格式: " + source_encoding['encoding'])

        if(source_encoding['encoding'] != "utf-8"):
            if(source_encoding['encoding'] == 'GB2312'):
                content = content.decode("GBK")
                content = content.encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            else:
                content = content.decode(source_encoding['encoding']).encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            print("转换完成")
            print("*************************")
        else:
            print("无需转换")
            print("*************************")

    except IOError as err:
        print("I/O error:{0}".format(err))

dir = os.getcwd()                                  #改成你要的地址
f = open(file = dir+"\\"+'f.txt',mode = 'w',encoding='utf-8')
for root, dirs, files in os.walk(dir,topdown=False):
    for name in files :
        file = os.path.join(root, name)        #获取dir目录和所有层级子目录的所有绝对路径文件名
        filetype=os.path.splitext(file)[1]   #文件扩展名
        
        if filetype != ".txt" or name == "f.txt":
            continue
        try :                           #尝试
            gbk_2_utf8(file)
        except :
            f.write(name)               #记录出错文件
            continue                    #出错就跳过
        
f.close()