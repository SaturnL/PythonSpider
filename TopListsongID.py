# -*- coding: utf-8 -*-

'''
    To get all the songs' id of certain top playlist
'''

import requests
from bs4 import BeautifulSoup
import general
import re

def getlistsongid(listid):
    num=listid
    play_url = general.toplist_url+str(num)     #形成待访问的网址
    s=requests.session()
    s=BeautifulSoup(s.get(play_url,headers=general.headers).content,"lxml")
    main=s.find('ul',{'class':'f-hide'})
    musid=[]
    for music in main.find_all('a'):
        urlx=str(music['href'])
        songid=re.sub('[/song?id=]','',urlx)     #提取数字id
        musid.append(songid)
    return musid