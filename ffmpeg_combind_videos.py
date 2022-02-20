# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:20:47 2020

@author: Aierlma
"""

import os
import re


def writeneedvids(path = os.getcwd()):
    FORMAT = ['.wmv', '.mp4', '.mkv', ".avi", "flv"]  # 想要更改的文件的格式
    files = [file for file in os.listdir(path) for item in FORMAT if os.path.splitext(file)[1]==item]
    with open(os.path.join(path, 'temp.txt'), 'w', encoding='utf-8') as tpf:
        for line in files:
            line1 = 'file' + ' '+"'"+line+"'"
            tpf.write(line1 + "\n")


def writeffmpeg(path = os.getcwd(), type = '.mp4'):
    name = re.sub(r'\s', '-', os.path.basename(path))
    with open(os.path.join(path, 'f.bat'), 'w', encoding='utf-8') as f:
        f.write(f"ffmpeg -f concat -safe 0 -i temp.txt -c copy {name}{type}")

def gettype(path = os.getcwd()):
    FORMAT = ['.wmv', '.mp4', '.mkv', ".avi", "flv"]  # 想要更改的文件的格式
    files = [file for file in os.listdir(path) for item in FORMAT if os.path.splitext(file)[1] == item]
    for i in files:
        type = os.path.splitext(i)[1]
    return type

def main():
    path = r'E:\Downloads\hypnolust\alexa'
    writeneedvids(path)
    writeffmpeg(path, gettype(path))

if __name__ == '__main__':
    main()