import os
count = 0 
a = os.getcwd()
files = os.listdir(a)
FORMAT = ['.jpg', '.JPG','.jpeg',".JPEG"] # 想要更改的文件的格式
image_names = [name for name in os.listdir(a) for item in FORMAT if os.path.splitext(name)[1] == item] # 想要更改的文件组成的列表
for line in image_names:
    print(line)
    
        path = a+"\\"+line
        print(path)
        filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
        
        for file in filelist:
            print(file)
        for file in filelist:   #遍历所有文件
            Olddir=os.path.join(path,file)   #原来的文件路径
            if os.path.isdir(Olddir):   #如果是文件夹则跳过
                continue
            filename=os.path.splitext(file)[0]   #文件名
            filetype=os.path.splitext(file)[1]   #文件扩展名
            Newdir=os.path.join(path,str(count).zfill(5)+line+filetype)  #用字符串函数zfill 以0从前补全所需位数
            os.rename(Olddir,Newdir)#重命名
            count+=1
    
