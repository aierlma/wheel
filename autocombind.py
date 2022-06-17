# -*- coding: utf-8 -*-
'''
Created on 2022/4/23 19:27

'''
import os
from file_rename import *

def ffmpeginpython(type, path):
    '''
    返回python中能用的ffmpeg语句
    Parameters
    ----------
    path 工作路径
    type 合成视频的格式应该是".mp4"这种格式

    Returns
    -------

    '''
    name = re.sub(r'\s', '-', os.path.basename(path))
    return f"ffmpeg -f concat -safe 0 -i temp.txt -c copy {name}{type}"

def main():
    '''
    针对一个文件夹之下有众多子文件夹的情况适用
    进入每个子文件夹，将子文件夹中的每个文件进行按需要重命名并合并ffmpeg
    Returns
    -------

    '''
    path = r"E:\Downloads"
    # path = os.getcwd()    #注释这一条与否决定你的工作路径
    f = os.listdir(path)         #path下面的子文件，包括文件夹，是个列表
    # for i in getparlist(r'E:\Downloads\stormy rose'):    #针对单一文件夹适用
    #     work(i, r'E:\Downloads\stormy rose')
    for i in f:            #i是f的元素，是单独的文件名，或者文件夹名，没有路径
        dir = os.path.join(path, i)   #dir是i的完整路径，经历下面的筛选，dir将只为文件夹
        if os.path.isdir(dir):    # 判断是否为文件夹
            for j in getparlist(dir, ty = ['.wmv', '.mp4', '.mkv', ".avi", ".flv"]):          #确保输入了你想要考虑的文件格式
                work(j, dir, r'[0-9]{1,3}\s(min)')      #确保输入了你想要删除的字符串,和想要考虑的文件格式
            writeneedvids(format=['.wmv', '.mp4', '.mkv', ".avi", ".flv"], path=dir)  # 将需要的合并的视频放进txt
            writeffmpeg(type=gettype(format=['.wmv', '.mp4', '.mkv', ".avi", ".flv"], path=dir),\
                        path=dir)  # 写下ffmpeg代码用来合并视频

            if "log.txt" in os.listdir(dir):
                c = ffmpeginpython(type = gettype(format=['.wmv', '.mp4', '.mkv', ".avi", ".flv"],path = dir),path = dir)
                os.system(f"e: && cd {dir} && {c}")        #执行ffmpeg合成,先进入e盘再进入dir路径再合成
                file_name=os.listdir(dir)            #dir文件夹下的文件列表
                file_dir = [os.path.join(dir,i) for i in file_name]        #dir文件夹下文件路径的列表
                nam = re.sub(r'\s', '-', os.path.basename(dir))           #文件夹名字把空格改成-
                type1 = gettype(format=['.wmv', '.mp4', '.mkv', ".avi", ".flv"],path = dir)  #dir下文件的后缀
                for _ in file_dir:
                    if _ != os.path.join(dir,nam+type1) and _ != "log.txt" :             #删除除了合成视频和log文件的所有文件
                        os.remove(_)


main()