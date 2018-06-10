#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 20:53:27 2018

@author: duanshuxi
"""

import general
from scipy.misc import imread
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud

def creatwordcloud(a):
    filename=a+'.txt'
    with open(filename,'r',encoding='utf-8') as f:
        music_subjects = f.readlines()
    
    musiclist = []
    for subject in music_subjects:
        if subject.isspace():
            continue
        word_list = pseg.cut(subject)     
        for word, flag in word_list:
            musiclist.append(word)
    
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "music.png")) #这个是改变词云形状的
    
    content = ' '.join(musiclist)
    wordcloud = WordCloud(font_path='simsun.ttc', 
                          background_color="white", 
                          max_words=300,
                          mask=mask_image).generate(content)  #此时的mask是默认的，可以通过指定改变
    
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('{}.png'.format(a))
    plt.show()
if __name__ == "__main__":
    for filename in general.top.keys():   
        creatwordcloud('LIST'+str(filename)+'lyric')
    for filename in general.artist.keys():   
        creatwordcloud('artist'+str(filename)+'lyric')
        creatwordcloud('comments'+str(filename))

    