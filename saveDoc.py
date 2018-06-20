#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/5 16:30
import os
import sys


def saveDocs(file, article):
    doc = open(file, 'a', encoding='utf-8')
    doc.write(article)
    doc.close()
