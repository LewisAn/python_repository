#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:51:37 2019

@author: apple
"""

from xlwt import *
import itchat

itchat.auto_login(hotReload=True)
#friends = itchat.get_friends()
chatroom = itchat.get_chatrooms(update=True)[1:]
#u = str(friends[10])
#v = str(chatroom[1])
#u = u.encode('unicode-escape').decode('utf-8')
#v = v.encode('unicode-escape').decode('utf-8')
#print(v)
filename = Workbook(encoding="utf-8")
table = filename.add_sheet('wechat_data')
#
ldata= []
#for x in num:
roomone_number = 0
roomtwo_number = 0
for room in chatroom:
    #print(room.get('NickName'))
    #print(room.get('MemberCount'))
    if "DECO1100" in room.get('NickName'):
        roomone_number = room['MemberCount']
    #if "CSSE1001" in room.get('NickName') and room.get('MemberCount') > 100:
        print(room)
        roomtwo_number = room['MemberCount']
    #if room.get('NickName') == '安仔家':
    #    print(room)
        #print("_____{}".format(room.get('MemberCount')))
#print("{}, {}".format(roomone_number,roomtwo_number))
    if "UQ最强大脑" in room.get('NickName'):
        print(list(room.keys()))
data = {
        '1':["DECO1100",roomone_number],
        '2':["CSSE1001",roomtwo_number]
        }
filename = Workbook(encoding="utf-8")
table = filename.add_sheet('wechat_data')
#
ldata= []
    
num = [a for a in data]

num.sort()
