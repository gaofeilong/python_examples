#!/usr/bin/python
# -*- coding: gbk -*-

import json,sys,random,datetime,ipaddress

def WhichToEatToday():
    eatList = [
        "西红柿鸡蛋",
        "清炒西兰花",
        "榄菜肉末四季豆",
        "葱花炒鸡蛋",
        "地三鲜",
        "老干妈炒鸡蛋",
        "干煸豆角",
        "小炒鱼豆腐",
        "农家小炒肉",
        "鸡蛋炒饼",
        "肉丝炒饼",
        "火腿炒饭",
        "扁豆焖面",
        "双椒焖面",
        "猪饲料",
    ]
    # 设置种子，当前天为种子
    # if (datetime.datetime.hour <= 12):
    random.seed(datetime.datetime.today().day)
    print("lunch: ", eatList[random.randrange(0, len(eatList))])
    # else:
    random.seed(datetime.datetime.today().day + 1)
    print("dinner:", eatList[random.randrange(0, len(eatList))])


############################################################
def main():
    WhichToEatToday()
    # print(ipaddress.ipaddress.ip)

main()
