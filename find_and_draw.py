import os
import shutil

dir = os.getcwd()                                  #改成你要的地址
#dir = r"E:\OneDrive - aierlmalee\MC\sale"
f = open(dir+"\\f.txt","r",encoding='utf-8')#你需要打开的txt，应该在此工作目录里
b = []
for line in f :
    c =  line.strip('\n')
    b.append(c)
lst = [0]#输入行序号,0代表全要
if lst == [0]:
    name = b
else :
    name = []
    for i in lst:
        name.append(b[i-1])#抽取所要的文件名
#os.mkdir(dir+'\\'+'temp')
f3 = open(dir+"\\original.txt",'w',encoding='utf-8')
f2 = open(dir+"\\not_finished.txt",'w',encoding='utf-8')
for root, dirs, files in os.walk(dir,topdown=False):     #游走dir目录和所有层级子目录。topdown表示是否先排序子文件夹
    for nm in files:
        file = os.path.join(root,nm)
        if nm in name:  
            source_path = file
            target_path = dir+"\\"+"temp"+'\\'+nm#输出地址
            if os.path.exists(target_path):#判断目标文件是否存在，存在则跳过
                continue
            shutil.copy(source_path, target_path)#复制操作
            print(nm+" finished")
            f3.write(file+"\n")
            continue
check = os.listdir(dir+"\\"+"temp")
if sorted(check) == sorted(name):
    print("all finished")
else :
    nf = []
    for i in name:
        for j in check:
            if i == j:
                continue
            if i in nf:
                continue
            nf.append(i)
            f2.write(i+"\n")
            print("1")
    print("something wrong")
    
f.close()
f3.close()
f2.close()