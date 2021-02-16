# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:12:55 2021

@author: AierlmaQuang
"""


import os 
import chardet

def guess_code(file):
    '''
    Used to guess encoding format.
    chardet is needed.

    Parameters
    ----------
    file : txt file
        The file which you want to guess encoding format.

    Returns
    -------
    source_encoding : dictionary
        It has 3 keys: encoding;confidence;language.
        language is not always useful.
        You can get output like guess_code(file)['encoding']
        Remember to change "GB2312" to "gbk"
    '''
    with open(file ,"rb") as f:
        content = f.read()
        source_encoding = chardet.detect(content)
    return source_encoding

help(guess_code)

for root, dirs, files in os.walk(os.getcwd()):          #游走文件夹，获得所有文件，不仅一层子文件夹
    for i in files:
        filename = os.path.splitext(i)[0]
        directory = os.path.join(root,i)

