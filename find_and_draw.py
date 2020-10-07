import os
import shutil
lst = [1,2,3,5,7]#输入行序号
a = os.getcwd()
f = open(a+"\\menu.TXT","r",encoding='utf-8')#你需要打开的txt，应该在此工作目录里
f2 = open(a+"\\not_finished.txt",'w',encoding='utf-8')
b = []
for line in f:
    c =  line.strip('\n')
    b.append(c)
d = []
for i in lst:
    d.append(b[i-1])#抽取所要的文件名
print(d)
path1 = "E:\\MC\\manga\\合集\\单行本"#查询地址1
file1 = os.listdir(path1)#path1下的所有文件
path2 = "E:\\MC\\manga\\合集\\散本"#查询地址2
file2 = os.listdir(path2)
for _ in d:
    if _ in file1:
        dire = path1+"\\"+_
        source_path = dire
        target_path = 'E:\\MC\\manga\\draw'+'\\'+_#输出地址
        if os.path.exists(target_path):#判断目标路径是否存在，存在则跳过
            continue
        shutil.copytree(source_path, target_path)#剪切操作记得粘贴回去
        print(_+" finished")
        continue
    elif _ in file2:
        dire = path2+"\\"+_
        source_path = dire
        target_path = 'E:\\MC\\manga\\draw2'+'\\'+_#输出地址
        if os.path.exists(target_path):#判断目标路径是否存在，存在则跳过
            continue
        shutil.copytree(source_path, target_path)#剪切操作记得粘贴回去
        print(_+" finished")
        continue
    print(_+'not finished')
    f2.write(_+'\n')
print("all finished")
f2.close()
f.close()