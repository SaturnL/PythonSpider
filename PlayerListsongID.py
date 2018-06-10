# -*- coding: utf-8 -*-

'''
    To get all the songs' id of certain player.
'''

import requests
from bs4 import BeautifulSoup
import general
import re

def GetArtistSongID(artistID):
    num=artistID
    play_url = general.artist_url+str(num)     #形成待访问的网址
    s=requests.session()
    s=BeautifulSoup(s.get(play_url,headers=general.headers).content,"lxml")
    main=s.find('ul',{'class':'f-hide'})
    songID=[]
    print('======================={}======================='.format(artistID))
    for music in main.find_all('a'):
        urlx=str(music['href'])
        Id=re.sub('[/song?id=]','',urlx)
        songID.append(Id)
    return songID