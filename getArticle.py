#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/5 15:11
# 每天定时获取 某技术网站5篇文章；保存到doc文档中，title为文章名字（表明时间）

import requests
from bs4 import BeautifulSoup as bs
import os
import time
import json
import getSoup
import saveDoc
# times = time.strftime('%m%d')
# def getArticle():
# urls = open('urls.json', 'r', encoding='utf-8')
# print(urls)
with open('urls.json', 'r', encoding='utf-8') as f:
    urls = json.load(f)
    # print(urls['sites'])
    urls = urls['sites']
    # print(urls)
    ii = 1
for url in urls:
    url = url['url'].strip()
    # print(url)
    soup = getSoup.getSoup(url)
    # file = time.strftime('%m%d')+str(ii)+'.doc'
    # print(file)
    if url == 'http://www.cnblogs.com/':
        article = soup.select('#editor_pick_lnk')
        # for article in article:
        #     articleUrl = article.get('href')
        #     print(articleUrl)
        # # articleReponse = requests.get(articleUrl)
        # # articleReponse.raise_for_status()
        # articleSoup = getSoup.getSoup(articleUrl)
        # articleTitle = articleSoup.select('#cb_post_title_url')
        # for articleTitle in articleTitle:
        #     articleTitle = articleTitle.get_text()
        #     print(articleTitle)
        #     file = articleTitle + '.doc'
        #     saveDoc.saveDocs(file, articleTitle)
        # articleBody = articleSoup.select('div#cnblogs_post_body')
        # for articleBody in articleBody:
        #     articleBody = articleBody.get_text()
        #     print(articleBody)
        #     saveDoc.saveDocs(file, articleBody)
        # # articleAll = articleTitle + articleBody
        # cite = '\n'+ '转自:'+ articleUrl
        # # saveDoc.saveDocs(file, articleTitle)
        # saveDoc.saveDocs(file, cite)

    # elif url == 'https://blog.csdn.net/':
    #     articleUrl = soup.select('.title a')
    #     for articleUrl in articleUrl:
    #         atUrl = articleUrl.get('href')
    #         print(atUrl)

    elif url == 'http://web.jobbole.com/category/basic-tech/':
        articleUrl = soup.find_all('a', {'class':'archive-title'})
        for articleUrl in articleUrl:
            atUrl = articleUrl.get('href')
            soup = getSoup.getSoup(atUrl)
            articleTitle = soup.select('.entry-header h1')
            articleBody = soup.select('.entry')
            for articleTitle in articleTitle:
                articleTitle = articleTitle.get_text()
                file = articleTitle + '.doc'
                saveDoc.saveDocs(file, articleTitle)

            for articleBody in articleBody:
                articleBody = articleBody.get_text()
                saveDoc.saveDocs(file, articleBody)
            print(atUrl)
    else:
        print('end')
print('爬取完毕')











