import os
import re
from word2number import w2n
from num2words import num2words
from ffmpeg_combind_videos import *

class File:
    '''
    建立file类，具有name，type，dir等固有属性
    以及delete特定字符串
    把英文数字变为阿拉伯数字
    格式化文件名
    '''

    def __init__(self, fullname, path):
        self.path = path
        self.newdir = None
        self.newfullname = None
        self.name = os.path.splitext(fullname)[0]  # 文件名
        self.type = os.path.splitext(fullname)[1]  # 文件扩展名
        self.dir = os.path.join(path, fullname)
        self.fullname = fullname

    def init(self):
        '''
        初始化函数，应该保证一个文件的属性改动了之后调用该函数
        Returns
        -------

        '''
        self.fullname = self.newfullname
        self.dir = self.newdir
        self.name = os.path.splitext(self.fullname)[0]  # 文件名
        self.type = os.path.splitext(self.fullname)[1]  # 文件扩展名

    def delete(self, particular_string):
        '''
        delet文件名中特定字符串，使用正则表达式
        需要import re
        import os
      :param particular_string:输入正则表达式
      :return:finish

      '''
        try:
            ps = re.search(particular_string, self.name, flags=0).group()
            print("delete " + str(ps))
            self.newfullname = self.fullname.replace(ps, '')
            self.newdir = os.path.join(self.path, self.newfullname)
            os.rename(self.dir, self.newdir)
            self.init()

        except:
            print('no need to delete')

        return "finish"

    def w2num(self):
        '''
        需要  from word2number import w2n
            from num2words import num2words
        把英文数字变为阿拉伯数字
        注意数字前后应该有空格
        :return:
        '''

        try:
            n_in_s = w2n.word_to_num(self.name)
            w_in_n = num2words(n_in_s).lower()
            self.newfullname = re.sub('('+str(w_in_n)+')', str(n_in_s), self.fullname, flags= re.I)

            self.newdir = os.path.join(self.path, self.newfullname)
            print(self.dir, self.newdir)
            os.rename(self.dir, self.newdir)
            self.init()
        except:
            pass


        return "finish"

    def autoformat(self):
        '''
        把数字放到文件最前面命名为两位数字
        如'asdfg5.mp4'会改为'05asdfg.mp4'
        :return:
        '''

        try:
            num = re.search(r'(?<!\d)[0-9]{1,2}(?!\d)', self.name, flags=0).group()
            self.newfullname = str(num).zfill(2)+re.sub(r'(?<!\d)[0-9]{1,2}(?!\d)', '', self.name)+self.type
            self.newdir = os.path.join(self.path, self.newfullname)
            os.rename(self.dir, self.newdir)
            self.init()
        except :
            print("pss")
            pass

def getparlist(path):
    '''
    获得路径内特定文件类型组成的列表
    Parameters
    ----------
    path 目的路径

    Returns list
    -------

    '''
    FORMAT = ['.wmv', '.mp4', '.mkv', ".avi", "flv"]  # 想要获取的文件的格式
    files = [file for file in os.listdir(path) for item in FORMAT if os.path.splitext(file)[1] == item]
    return files

def work(name, path, dele):
    '''
    调用File类，运行删除，w2n，自动格式化等任务
    :param name: 文件名（包含后缀）
    :param path: 文件路径
    :param dele: 欲删除的字符（正则表达式）
    :return:
    '''
    vid = File(name, path)
    vid.delete(dele)
    vid.w2num()
    vid.autoformat()
    writeneedvids(path)  # 将需要的合并的视频放进txt
    writeffmpeg(path, gettype(path))   #写下ffmpeg代码用来合并视频

def main():
    '''
    针对一个文件夹之下有众多子文件夹的情况适用
    进入每个子文件夹，将子文件夹中的每个文件进行按需要重命名
    Returns
    -------

    '''
    path = r"E:\Downloads\hypnolust"
    f = os.listdir(path)

    for i in f:
        dir = os.path.join(path, i)
        if os.path.isdir(dir):    # 判断是否为文件夹
            for j in getparlist(dir):
                work(j, dir, r'[0-9]{1,3}\s(min)')

if __name__ == '__main__':
    main()
