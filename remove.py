#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 12:41:36 2018

@author: duanshuxi
"""

import general
import re
def do(ID):
    
    oname=str(ID)+'.txt'
    print('removing {}'.format(oname))
    with open(oname,encoding='utf-8') as f:
        r=f.readlines()
        res=r[0]
        res=re.sub('作词','',res)
        res=re.sub('作曲','',res)
        res=re.sub('编曲','',res)
        res=re.sub('混音','',res)
    
    name='artist'+str(ID)+'lyric.txt'
    with open(name,'w',encoding='utf-8') as f:
        f.write(res)
    print('finished!')


if __name__ == "__main__":
#    listid=general.top.keys()
#    for ID in listid:
#        do(ID)
    listid=general.artist.keys()
    for ID in listid:
        do(ID)