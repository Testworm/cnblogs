#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/5 12:47
# 实现功能：爬取top100作者,获取其访问URL,自动下载TOP N文章（标题,摘要,内容）,保存到doc
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os

# 获取Soup
def getSoup(url):
    response = requests.get(url)
    response.raise_for_status()
    res = response.content
    soup = bs(res, 'html.parser')
    return soup

# 获取Top N作者信息
def getTop100():
    url = 'https://www.cnblogs.com/'
    cnb = webdriver.Firefox()
    cnb.get(url)
    aRank = cnb.find_element_by_id("blogger_list")
    # webdriver可以实现获取页面部分元素
    InnerElement = aRank.get_attribute('innerHTML')

    # response = requests.get(url)
    # response.raise_for_status()
    # res = response.content
    soup = bs(InnerElement, 'html.parser')
    # print(soup)
    idList = soup.select('a')
    # for id in idList:
    #     print(id)
    return idList[:-2]

# ids = getTop100()
# print(ids)
# for id in ids:
#     print(id.get('href'))


def getArticleByAuthor(name):
    # if ' ' in name:
    #     name = '-'.join(list(name))
    # else:
    #     name = name
    # print(name)
    for i in range(1, 5):
        url = 'http://www.cnblogs.com/'+name+'/default.html?page='+str(i)+''
        # response = requests.get(url)
        # response.raise_for_status()
        # res = response.content
        soup = getSoup(url)
        titles = soup.select('.postTitle a')
        # article = open('article')
        ii = 0
        for title in titles:
            tit = title.text.strip()
            tit = tit +'.doc'
            article = open(tit, 'wb', encoding='utf-8')
            print(title.text+'-'+title.get('href'))


# def getArticle():



authors = getTop100()
for author in authors[1:]:
    author = author.text.strip()
    print(author)
    # getArticleByAuthor(author)



