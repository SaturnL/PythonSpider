# -*- coding: utf-8 -*-
'''
    This is the general documents that needed in other
    programes.
'''

headers={
    'Host': 'music.163.com',
    'Origin': 'http://music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'http://music.163.com/song?id=557581284'
}#used for requests

userid = {
    'username': 'Pythonmusic',
    'password': 'wangyidafahao',
    'rememberLogin': 'true'
}#used for logining in


#urls needed to request
toplist_url = 'http://music.163.com/discover/toplist?id='
lyric_url = "http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1"
play_url = "http://music.163.com/discover/playlist/?order=hot&cat={}&limit=35&offset={}"
music_url = "http://music.163.com/api/playlist/detail?id="
artist_url = "http://music.163.com/artist?id="
comments_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_{}"


#The id of some top lists
top = {
    19723756: '云音乐飙升榜',#
    3779629: '云音乐新歌榜',#
    2884035: '网易原创歌曲榜',#
    3778678: '云音乐热歌榜',#
    1978921795: '云音乐电音榜',
    991319590: '云音乐嘻哈榜',#
    10520166: '云音乐新电力榜',#
    180106: 'UK排行榜周榜',#
    60198: '美国Billboard周榜',#
    11641012: 'iTunes榜'#
}

#list out the artist ID
artist = {
    2116:'陈奕迅',
    5781:'薛之谦',
    3684:'林俊杰',
    6452:'周杰伦',
    4292:'李荣浩',
    7214:'蔡健雅',
    7763:'邓紫棋',
    893259:'金玟岐',
    9621:'王菲',
    178059:'Bruno Mars',
    35531:'Justin Bieber',
    32665:'Eminem',
    96266:'Maroon 5',
    98105:'OneRepublic',
    98351:'OneDirection',
    45839:'Westlife',
    46487:'Adele',
    72724:'Rihanna',
    44266:'Taylor Swift',
    64147:'Lady Gaga',
    48161:'Ariana Grande'
}