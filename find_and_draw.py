import os
import shutil
dir = os.getcwd()                                  #改成你要的地址
f = open(dir+"\\1.txt","r",encoding='utf-8')#你需要打开的txt，应该在此工作目录里
b = []
for line in f :
    c =  line.strip('\n')
    b.append(c)
lst = [1，2，3，5，8]#输入行序号,0代表全要
if lst == [0]:
    name = b
else :
    name = []
    for i in lst:
        name.append(b[i-1])#抽取所要的文件名
os.mkdir(dir+'\\'+'temp')
f3 = open(dir+"\\original.txt",'w',encoding='utf-8')
for root, dirs, files in os.walk(dir,topdown=False):     #游走dir目录和所有层级子目录。topdown表示是否先排序子文件夹
    for nm in files:
        if nm in name:
            file = os.path.join(root,nm)
            source_path = file
            target_path = dir+"\\"+"temp"+'\\'+nm#输出地址
            if os.path.exists(target_path):#判断目标文件是否存在，存在则跳过
                continue
            shutil.copy(source_path, target_path)#复制操作
            print(nm+" finished")
            f3.write(file+"\n")
            continue
check = os.listdir(dir+"\\"+"temp")
if check == name:
    print("all finished")
else :
    f2 = open(dir+"\\not_finished.txt",'w',encoding='utf-8')
    for i in name :
        if i in check:
            continue
        f2.write(i)
    f2.close()
    print("something wrong")
f.close()
f3.close()