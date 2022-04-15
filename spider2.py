# -*- coding: utf-8 -*-
'''
Created on 2022/4/15 11:43
加强版爬虫脚本
'''
import requests
import time
import os
import random
import re
import wget
'''保存路径'''
path = r'./save'

'''设置socks5代理'''
proxy = '127.0.0.1:15460'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}

'''目标网址'''
def url(alt):
    url = 'https://xcvdfqw.info/home.php?mod=space&uid=410467&do=thread&view=me&order=dateline&from=space&page='+str(alt)
    return url
'''设置请求头'''
def headers():
    headers = {}
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
    headers['User-Agent'] = random.choice(user_agent_list) #随机选择请求头防止被断联
    headers['Cookie'] = ''
    #自己设定cookie，如果获取的信息需要登录
    return headers

def url2(alt=''):
    url = f'https://xcvdfqw.info/forum.php?mod=viewthread&tid={alt}'
    return url

def main():
    if os.path.exists(path) == False:  # 没有就创建
        os.mkdir(path)
    try:
        '''对url获取特定网址并下载'''
        with open('save.txt','w',encoding='utf-8')as f:
            for i in range(1, 21):
                    response = requests.get(url(i), headers=headers())
                    txt = response.text
                    tid = re.findall(r'(?<=tid=)[0-9]*(?=.*Pcolle)', txt, flags=0)
                    title = re.findall(r'(?<=target=._blank. >).*Pcolle.*(?=</a>)', txt, flags=0)
                    link = [f'https://xcvdfqw.info/forum.php?mod=viewthread&tid={i}'for i in tid]
                    t = list(zip(link,title))
                    f.write(str(t)+'\n')
                    for j in range(len(tid)):                 #对每一个单独的页面
                        resp = requests.get(url2(tid[j]), headers=headers())
                        txt1 = resp.text
                        piclink = re.findall(r'http.*jpg|(?<=zoomfile=\")https.*?gif', txt1, flags=0)  #需要下载图片的链接
                        picpath = os.path.join(path, re.sub(r'(\?)|(\*)|:|"|<|>|(\\)|(\/)|(\|) ',r'',title[j]))
                        try :
                            print(piclink)
                            if os.path.exists(picpath) == False:  # 没有就创建
                                os.mkdir(picpath)
                            for _ in range(len(piclink)):
                                wget.download(piclink[_], picpath)  #若为文件夹，应提前创建
                        except:
                            with open("./logpic.txt", 'a', encoding='utf-8') as logpic:
                                logpic.write(link[j] + title[j] + '\n')
                        # dlink = re.findall(r'(?<=<a href=")https.*(?=".onmouseover)', txt1, flags=0)  #需要下载文件的链接
                        # path1 = os.path.join(path,re.sub(r'(\?)|(\*)|:|"|<|>|(\\)|(\/)|(\|) ',r'',title[j])+'.rar')  #下载后保存的名字
                        # print(re.sub(r'(\?)|(\*)|:|"|<|>|(\\)|(\/)|(\|) ',r'',title[j]))
                        # try:
                        #     wget.download(dlink[0],path1)           #下载文件
                        # except:
                        #     with open("./log.txt",'a',encoding='utf-8') as log:
                        #         log.write(link[j]+title[j]+'\n')
                        # time.sleep(1)                #设置时间防止断联

    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)

if __name__ == '__main__':
    main()