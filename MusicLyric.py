# -*- coding: utf-8 -*-


#encoding=utf8
import requests
from bs4 import BeautifulSoup
import general

url='http://music.163.com/song?id=557581284'
k=requests.session()
k=BeautifulSoup(k.get(url,headers=general.headers).content,"lxml")
print(k)