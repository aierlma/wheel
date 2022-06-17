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
proxy = '127.0.0.1:15846'
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
                    response = requests.get(url(i),headers=headers(), proxies=proxies)
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