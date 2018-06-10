# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:10:54 2018

@author: Saturn
"""

import general
import MusicComments
import PlayerListsongID

artistlist=list(general.artist.keys())
for artist in artistlist:
    songs=PlayerListsongID.GetArtistSongID(artist)
    comments=''
    for song in songs:
        comments=comments+MusicComments.getcomments(song)+' '
    name = 'comments'+str(artist)+'.txt'
    with open(name,'w',encoding='utf-8') as f:
        f.write(comments)
    print('Finished!')