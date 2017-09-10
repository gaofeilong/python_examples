#!/bin/python
# -*- coding: gbk -*-

import json

"""
# 文本预处理：
# replace command in vim: :%s/[-,.;"()?!\[\]]/ /g
# 全部变为小写：全选u
# 去掉数字：:%s/\d//g
"""

def GetWords(file, words):
    content = ""
    for i in open(file).readlines():
        content += i[:len(i) - 1]
    for w in list(content.split()):
        if len(w) < 3:
            continue
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

def SortPrint(words):
    cnts = sorted(set(list(words.values())), reverse=True)
    for cnt in cnts:
        for k,v in words.items():
            if v == cnt:
                print("%s: %s" %(k.ljust(25), ("%d" % v).rjust(5)))


words = {}
GetWords("en.txt", words)
SortPrint(words)

# print(json.dumps(words, indent=4))
