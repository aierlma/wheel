# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:12:55 2021

@author: AierlmaQuang
"""


import os 
import chardet

def guess_code(file):
    '''
    Used to guess encoding format.
    import chardet is needed.

    Parameters
    ----------
    file : txt file
        The file which you want to guess encoding format.

    Returns
    -------
    source_encoding : dictionary
        It has 3 keys: encoding;confidence;language.
        language is not always useful.
        You can get output like guess_code(file)['encoding']
        Remember to change "GB2312" to "gbk"
    '''
    with open(file ,"rb") as f:
        content = f.read()
        source_encoding = chardet.detect(content)
    return source_encoding

help(guess_code)

for root, dirs, files in os.walk(os.getcwd()):          #游走文件夹，获得所有文件，不仅一层子文件夹
    for i in files:
        filename = os.path.splitext(i)[0]
        directory = os.path.join(root,i)

def base64toimg(b64,format):
    '''
    Transform base64 to image
    import base64 is needed

    Parameters
    ----------
    b64 : string
        That is the base64 code
    format:string
        That is the img format(like png,jpg,etc.)


    Returns
    -------
    'succesful'
    '''
    img_str = str(b64)
    img_data = base64.b64decode(img_str)
# 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。
    with open('001.'+str(format), 'wb') as f:
        f.write(img_data)
    return 'succesful'


def get_baidu_access_token(AK,SK):
    '''
    Used to get baidu access token
    import requests is needed

    Parameters
    ----------
    AK : string
        That is API key
    SK : string
        That is secret key


    Returns
    -------
    return a list 
    the first element is access_token 
    2nd is response.json()
    you can get output like get_baidu_access_token(AK,SK)[0]
    '''
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+str(AK)+'&client_secret='+str(SK)
    response = requests.get(host)
    access_token = response.json()['access_token']
    return [access_token,response.json()]

import PIL.Image as Image
import os 

IMAGES_FORMAT = ['.jpg', '.JPG','.jpeg',".JPEG"] # 图片格式
image_names = [name for name in os.listdir(os.getcwd()) for item in IMAGES_FORMAT if
os.path.splitext(name)[1] == item]
example = Image.open(image_names[0])
wide , height = example.size
#this is used to get wide and height of a image