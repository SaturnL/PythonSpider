# -*- coding: utf-8 -*-

headers={
    'Host': 'music.163.com',
    'Origin': 'http://music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'http://music.163.com/song?id=557581284'
}

userid = {
    'username': 'Pythonmusic',
    'password': 'wangyidafahao',
    'rememberLogin': 'true'
}

comment_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}/?csrf_token="
lyric_url = "http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1"
play_url = "http://music.163.com/discover/playlist/?order=hot&cat={}&limit=35&offset={}"
music_url = "http://music.163.com/api/playlist/detail?id="
#playlist_api = "http://music.163.com/api/playlist/detail?id={}&upd"
#music_api = "http://music.163.com/api/song/detail/?id={}&ids=[{}]"
#playlist_add_api = "http://music.163.com/weapi/playlist/manipulate/tracks?csrf_token={}"
#login_api = "http://music.163.com/weapi/login/cellphone"

top = {
    19723756: '云音乐飙升榜',
    3779629: '云音乐新歌榜',
    2884035: '网易原创歌曲榜',
    3778678: '云音乐热歌榜',
    1978921795: '云音乐电音榜',
    991319590: '云音乐嘻哈榜',
    10520166: '云音乐新电力榜',
    180106: 'UK排行榜周榜',
    60198: '美国Billboard周榜',
    11641012: 'iTunes榜'
}