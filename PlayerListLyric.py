# -*- coding: utf-8 -*-
'''
    Get all the songs' lyric of certain artist.
'''

import PlayerListsongID
import MusicLyric
import general

IDlist=list(general.artist.keys())
for ID in IDlist:
    print('================={}================='.format(ID))        
    IDlist=PlayerListsongID.GetArtistSongID(ID)             #构建作者内所有歌曲ID的列表
    lyric=''
    for id in IDlist:
        l = MusicLyric.getlyric(id)                  #获得该id的歌曲的歌词
        lyric += l
    
    name=str(ID)+'.txt'            #构成将爬取下来的歌词写入txt文件
    with open(name,'w',encoding='utf-8') as f:
        f.write(lyric)