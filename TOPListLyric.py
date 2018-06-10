# -*- coding: utf-8 -*-

'''
    Get all the songs' lyric of certain top playlist.
'''


import general
import TopListsongID
import MusicLyric

listnumber=list(general.top.keys())          #访问general.py得到toplists的ID值
for listid in listnumber:
    #listid=listnumber[0]                    #用于测试
    print('================={}================='.format(general.top[listid]))        # 显示已完成的进度
    IDlist=TopListsongID.getlistsongid(listid)          #构建某一个歌单内所有歌曲ID的列表
    lyric=''
    for id in IDlist:
        l = MusicLyric.getlyric(id)                  #获得该id的歌曲的歌词
        lyric += l
    name=str(listid)+'.txt'            #构成将爬取下来的歌词写入txt文件
    with open(name,'w',encoding='utf-8') as f:
        f.write(lyric)
    print('Finished!')