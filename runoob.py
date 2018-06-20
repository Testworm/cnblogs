# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 23:26
# @Author  : Torre
# @Email   : klyweiwei@163.com

import requests
from bs4 import BeautifulSoup as bs
import os
import time
import getSoup
import saveDoc

def runoob():
    url = 'http://www.runoob.com/python3/python3-tutorial.html'
    soup = getSoup.getSoup(url)
    urls = soup.select('div#leftcolumn a')
    for url in urls:
        url = url.get('href')
        url = 'http://www.runoob.com'+ url
        print(url)
        soup = getSoup.getSoup(url)
        articleBody = soup.select('.article-intro')
        for articleBody in articleBody:
            articleBody = articleBody.get_text()
            saveDoc.saveDocs('runoob菜鸟教程.doc', articleBody)

runoob()

