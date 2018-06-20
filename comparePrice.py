# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 0:12
# @Author  : Torre
# @Email   : klyweiwei@163.com
# 比价，从天猫上获取某一商品最低价，并打印
# A网站把商品标题爬取出来，存入文档，再通过天猫搜相同商品
# 通过excel的商品信息，搜索天猫相同商品的价格
# 天猫》 价格、图片、店铺

import getSoup
import saveDoc
from bs4 import BeautifulSoup
import os

