# -*- coding: utf-8 -*-
'''
    Form function：Using the id of certain song to get the lyric of the song
'''

import requests
from bs4 import BeautifulSoup
import general
import json
import re

def getlyric(id):
    '''using the id to find the id's lyric'''
    url=id
    lyric_url=general.lyric_url.format(url)
    #print(lyric_url)
    k=requests.session()
    k=BeautifulSoup(k.get(lyric_url,headers=general.headers).content,'lxml')
    k = json.loads(k.find('p').text)     #在返回的Json文件中找到歌词的部分
    try:
        lyric=k['lrc']['lyric']
        res=re.sub('[\[\]0123456789:.\n]','',lyric)
    except KeyError:             #防止有些歌曲因为是纯音乐而形成无法提取的状况
        res=''
    return res

