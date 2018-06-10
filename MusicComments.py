# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 22:22:57 2018

@author: Saturn
"""

import requests
from bs4 import BeautifulSoup
import general
import json

headers={
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",    
    'Host': 'music.163.com',
    'Origin': 'http://music.163.com',
    'Referer': 'http://music.163.com/song?id=571340283',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
}       

#songID ='186016'
def getcomments(songID):
    '''get the comments of a song'''
    url=general.comments_url.format(songID)
    html=requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    try:
        res=json.loads(soup.text)
        comment=res['hotComments']
        comments=''
        for co in comment:
            comments =comments+co['content']+' '
    except json.JSONDecodeError:
        comments=' '
    return comments