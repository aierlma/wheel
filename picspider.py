# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:03:39 2021

@author: AierlmaQuang
"""

import requests
import time
import os
import random
import re
'''保存路径'''
path = r'./'

'''设置socks5代理'''
proxy = '127.0.0.1:15460'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}

'''目标网址'''
def url(alt):
    url = 'http://book.ucdrs.superlib.net/search?channel=search&gtag=&sw=%E9%82%AA%E7%81%AB&ecode=utf-8&Field=all&Sort=&adminid=&btype=&seb=0&pid=0&year=&sectyear=&showc=0&fenleiID=&searchtype=&authid=0&exp=0&expertsw=&Pages='+str(alt)
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
    return headers

if __name__=='__main__':
    if os.path.exists(path) == False: # 没有就创建
        os.mkdir(path)
    try:
        for i in range(1,33):
            response = requests.get(url(i),headers=headers(), proxies=proxies)# 使用headers避免访问受限
            txt = response.text
            t = re.findall(r'(?<=title" value=").*?(?=">)',txt,flags=0)
            print(t,i)
        
        '''for i in range(47):
            response = requests.get(url(i+1),headers=headers(), proxies=proxies)# 使用headers避免访问受限
            data = response.content
            with open(path+r'/%s.jpg'%str(i+1).zfill(2), 'wb') as f:
                f.write(data)
            time.sleep(1)   '''             #设置时间防止断联
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)