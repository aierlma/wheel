import os
a = os.getcwd()
file = os.listdir(a)
f = open(a+"\\"+'1.txt','w',encoding = 'utf-8')
for i in file:
    f.write(i+'\n')
f.close()
print('task finished')
