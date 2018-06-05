# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import general
numlist=list(general.top.keys())
for num in numlist:
    play_url = 'http://music.163.com/discover/toplist?id='+str(num)
    s=requests.session()
    s=BeautifulSoup(s.get(play_url,headers=general.headers).content,"lxml")
    main=s.find('ul',{'class':'f-hide'})
    musurl=[]
    print('======================={}======================='.format(general.top[num]))
    for music in main.find_all('a'):
        urlx='http://music.163.com'+music['href']
        musurl.append(urlx)
        print('{}'.format(music.text))