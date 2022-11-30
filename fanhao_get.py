# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:32:04 2021

@author: AierlmaQuang
"""
import random

import requests
import os
import re
'''保存路径'''
path = r'./save'

'''设置socks5代理'''
proxy = '127.0.0.1:15846'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}

'''目标网址'''
def url(alt):
    url = 'https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=21npd0000'+str(alt)
    return url
'''设置请求头'''
def headers():
    headers = {}
    user_agent_list = [
        'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
        'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7',
        'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e YisouSpider/5.0 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 4.0; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/59.0.3071.92',
        'Mozilla/5.0 (Linux; Android 6.0.1; SOV33 Build/35.0.D.0.326) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.6.1.1',
        'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-J7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.7.977 Mobile Safari/537.36',
        'Mozilla/6.0 (Linux; Android 8.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Mobile Safari/537.36'
        ]
    headers['User-Agent'] = random.choice(user_agent_list) #随机选择请求头防止被断联
    headers['Connection'] = 'close'
    # headers['Cookie'] = ''
    #自己设定cookie，如果获取的信息需要登录
    return headers
x = os.getcwd()
# c = ['https://www.dmmbus.blog/search/%E6%9E%97%E3%82%86%E3%81%AA','https://www.dmmbus.blog/search/%E6%9E%97%E3%82%86%E3%81%AA/2']  #查找的网页

with open(x+'//result.txt',"w") as f:
    print(proxies)
    response = requests.get(url(3),headers=headers(), proxies=proxies)

    b = response.text
    print(b)
    t = re.findall(r'(?<=<h1 id=\"title\" class=\"item fn\">).*?(?=<\/h1>)',b,flags=0)
    print(t)
    # for i in range(4):
    #     response = requests.get(url(i+1), headers=headers())
    #     b = response.text
    #     print(b)
        
        
        # t = re.findall(r'[A-Za-z]{2,5}-[0-9]{3}',b,flags=0)
        #
        # t = list(set(t))
        # print(t)
        # for i in t:
        #     f.write(i+',')