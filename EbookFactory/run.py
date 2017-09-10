#!/bin/python
# -*- coding: gbk -*-
from pyh import *
import os, re, shutil

dest = "dest"
book = "book"
indexHtml = "index.html"
catalogHtml = "catalog.html"

def CreateLink(myPage, chapter, lang):
    link = {
        "en": { 
            "home": "HomePage",
            "catalog": "Catalog",
            "lang": "Chinese",
            "next": "NextChapter",
            "prev": "PreviousChapter",
        },
        "cn": {
            "home": "主页",
            "catalog": "目录",
            "lang": "英文",
            "next": "下一章",
            "prev": "上一章",
        },
    }
    
    if lang != "cn" and lang != "en":
        return
    switch = list(link.keys())[len(link) - list(link.keys()).index(lang) - 1]
    myTable = myPage << table(width = "100%", align = "center")
    myTr   = myTable << tr()
    myTd   = myTr << td(width = "35%")
    mySpan = myTd << span(style = "float:left")
    mySpan << a(link[lang]["home"], href = "../../" + indexHtml)
    mySpan = myTd << span(style = "float:left;margin-left:10px")
    mySpan << a(link[lang]["catalog"], href = "../" + catalogHtml)
    myTd   = myTr << td(width = "20%", align="center")
    myTd   << a(link[lang]["lang"], href = "../%s/%d.html" %(switch, int(chapter)))
    myTd   = myTr << td(width = "45%")
    mySpan = myTd << span(style = "float:right")
    mySpan << a(link[lang]["next"], href = "%d.html" %(int(chapter) + 1))
    mySpan = myTd << span(style = "float:right;margin-right:10px")
    mySpan << a(link[lang]["prev"], href = "%d.html" %(int(chapter) - 1))

def Split(bookName, lang, catalog):
    lastFile = ''
    paragraph = ''
    isCatalog = True
    
    myPage = PyH()
    for line in open(book + "/" + bookName + "/" + lang + ".txt").readlines():
        if isCatalog:
            if not re.match(r"=+$", line):
                catalog[lang].append(line)
                continue
            isCatalog = False
        else:
            if line in catalog[lang]:
                if lastFile:
                    CreateLink(myPage, lastFile.split("/")[-1].split(".")[0], lang)
                    myPage.printOut(lastFile)
                myPage = PyH()
                myPage.addCSS("../../src/css/style.css")
                myPage << h1(line, align = "center")
                CreateLink(myPage, line.split()[0], lang)
                lastFile = "%s/%s/%s/%d.html" %(dest, bookName, lang, int(line.split()[0]))
            else:
                paragraph = paragraph + " " + line[:len(line) - 1]
                if len(line) < 55:
                    myPage << p(paragraph)
                    paragraph = ''
                else:
                    if line[-2] in '."。':
                        myPage << p(paragraph)
                        paragraph = ''
    CreateLink(myPage, lastFile.split("/")[-1].split(".")[0], lang)
    myPage.printOut(lastFile)

def CreateContent():
    for i in os.listdir(book):
        catalog = {"en":[], "cn":[]}
        if re.match(r"^[a-z]", i):
            continue
        for j in os.listdir(book + "/" + i):
            Split(i, j.split(".")[0], catalog)
        myPage = PyH()
        myPage.addCSS("../src/css/style.css")
        myPage << h1(i, align = "center")
        myPage << table(align = "center") << tr() \
               << td(align = "center") << a("首页", href = "../" + indexHtml)
        myTable = myPage << table(border = "0", width = "100%", align = "center")
        for j in range(len(catalog["en"])):
            myTr = myTable << tr()
            myTr << td() << a(catalog["en"][j], href = "%s/%d.html" %("en", j + 1))
            myTr << td() << a(catalog["cn"][j], href = "%s/%d.html" %("cn", j + 1))
        myPage.printOut(dest + "/" + i + "/" + catalogHtml)

def CreateIndex():
    enSrc = "en.txt"
    cnSrc = "cn.txt"
    lang = ["en", "cn"]

    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(book, dest)

    page = PyH()
    page.addCSS("src/css/style.css")
    page << h1("My Private Library", align = "center")
    myTable = page << table(align = "center", border = "0")
    for i in os.listdir(dest):
        if re.match(r"^[a-z]", i):
            continue
        myTable << tr() << td(align = "center", height = "40px") \
                        << a(i, href = "%s/%s" %(i, catalogHtml))
        os.unlink(dest + "/" + i + "/" + enSrc)
        os.unlink(dest + "/" + i + "/" + cnSrc)
        for j in range(len(lang)):
            os.mkdir(dest + "/" + i + "/" + lang[j])
    page.printOut(dest + "/" + indexHtml)



CreateIndex()
CreateContent()
