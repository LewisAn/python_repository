#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:51:37 2019

@author: apple
"""
import json
import pandas
import itchat

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
chatrooms = itchat.get_chatrooms(update=True)[1:]
# json_friends = json.load(friends)
# json_chatrooms = json.load(chatrooms)
# roomone_number = 0
# roomtwo_number = 0
# for room in chatrooms:

#     if "DECO1100" in room.get('NickName'):
#         roomone_number = room['MemberCount']
#         print(room)
#         roomtwo_number = room['MemberCount']

#     if "UQ最强大脑" in room.get('NickName'):
#         print(list(room.keys()))

# data = {
#         '1':["DECO1100",roomone_number],
#         '2':["CSSE1001",roomtwo_number]
#         }
