# -*- coding: utf-8 -*-

# -- Sheet --

import requests

from bs4 import BeautifulSoup

r = requests.get('https://www.newsinlevels.com/products/albino-tortoise-level-1/')

r.status_code

soup = BeautifulSoup(r.content, 'lxml')   #解析网页用，后面的参数可以用"lxml"或者"html.parser"
print(soup.prettify())        #将树状解析变为字符，同时美化

p1 = soup.find("title")    #找一次
p1

p2 = soup.find_all("p")    #找全部
p2

p3 = soup.find_all('p', {'style': 'text-align: center;'})
p3

paragraphs = soup.find_all('p', {'style': 'text-align: center;'})  #找全部中属性符合的

for p in paragraphs:
    print(p.text + '\n')

a = soup.find_all('a')
for i in a:
    print(i.get("href"))      #获取标签中属性值

