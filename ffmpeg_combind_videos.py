# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:20:47 2020

@author: Aierlma
"""

import os
import re


def writeneedvids(path=os.getcwd(), format = [".flv"]):
    '''
    可以把你需要合成的视频写在tempt.txt中
    Parameters
    ----------
    path 是你需要工作的路径
    format 是列表，应该输入类似['.wmv', '.mp4', '.mkv', ".avi", ".flv"]，代表你需要的格式

    Returns
    -------

    '''
    # format = ['.wmv', '.mp4', '.mkv', ".avi", ".flv"]  # 想要更改的文件的格式
    files = [file for file in os.listdir(path) for item in format if os.path.splitext(file)[1] == item]
    with open(os.path.join(path, 'temp.txt'), 'w', encoding='utf-8') as tpf:
        for line in files:
            line1 = 'file' + ' ' + "'" + line + "'"
            tpf.write(line1 + "\n")


def writeffmpeg(path=os.getcwd(), type='.mp4'):
    '''
    写一个合成视频的ffmpeg文件
    Parameters
    ----------
    path 工作路径
    type 合成视频的格式应该是".mp4"这种格式

    Returns
    -------

    '''
    name = re.sub(r'\s', '-', os.path.basename(path))
    with open(os.path.join(path, 'f.bat'), 'w', encoding='utf-8') as f:
        f.write(f"ffmpeg -f concat -safe 0 -i temp.txt -c copy {name}{type}")


def gettype(path=os.getcwd(), format = ['.wmv', '.mp4', '.mkv', ".avi", ".flv"]):
    '''

    Parameters
    ----------
    path 工作路径
    format 想要的考虑的格式的列表

    Returns
    -------

    '''
    # format = ['.wmv', '.mp4', '.mkv', ".avi", ".flv"]  # 想要更改的文件的格式
    files = [file for file in os.listdir(path) for item in format if os.path.splitext(file)[1] == item]
    for i in files:
        type = os.path.splitext(i)[1]
    return type


def main():
    path = r'E:\Downloads'
    writeneedvids(path)
    writeffmpeg(path, gettype(path,['.flv']))


if __name__ == '__main__':
    main()
