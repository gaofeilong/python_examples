#!/usr/bin/python
# -*- coding: gbk -*-

import json,sys,random,datetime,ipaddress

def WhichToEatToday():
    eatList = [
        "����������",
        "�峴������",
        "魲���ĩ�ļ���",
        "�л�������",
        "������",
        "�ϸ��賴����",
        "���Զ���",
        "С���㶹��",
        "ũ��С����",
        "��������",
        "��˿����",
        "���ȳ���",
        "�ⶹ����",
        "˫������",
        "������",
    ]
    # �������ӣ���ǰ��Ϊ����
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
