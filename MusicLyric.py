# -*- coding: utf-8 -*-


#encoding=utf8
import requests
from bs4 import BeautifulSoup
import general
import json

url='557581284'
lyric_url=general.lyric_url.format(url)
print(lyric_url)
k=requests.session()
k=BeautifulSoup(k.get(lyric_url,headers=general.headers).content,'lxml')
k = json.loads(k.find('p').text)
lyric=k['lrc']['lyric']
lyric.replace('')