# -*- coding: utf-8 -*-
'''
    To get the list of some top lists.
'''

import requests
from bs4 import BeautifulSoup
import general

numlist=list(general.top.keys())                #访问general文件
for num in numlist:
    play_url = general.toplist_url+str(num)       #形成待访问url
    s=requests.session()
    s=BeautifulSoup(s.get(play_url,headers=general.headers).content,"lxml")
    main=s.find('ul',{'class':'f-hide'})        #查找出待筛选字段
    musurl=[]
    print('======================={}======================='.format(general.top[num]))
    for music in main.find_all('a'):
        urlx='http://music.163.com'+music['href']
        musurl.append(urlx)                    #构建歌曲网址的url
        print('{}'.format(music.text))