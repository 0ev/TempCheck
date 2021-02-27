import client
from packet import Packet
import bson
import time
import json
import os
import hashlib
import mimetypes
import httpApi

from datetime import datetime, time

def is_time_between(begin_time, end_time, check_time=None):
    check_time = check_time or datetime.utcnow().time()
    
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: 
        return check_time >= begin_time or check_time <= end_time

def check_if_done_am():
    file = open("Kakao\check.txt","r")
    a = file.readline()
    file.close()
    if a == "am":
        return False
    else:
        file = open("Kakao\check.txt","w")
        file.write("am")
        file.close()
        return True

def check_if_done_pm():
    file = open("Kakao\check.txt","r")
    a = file.readline()
    file.close()
    if a == "pm":
        return False
    else:
        file = open("Kakao\check.txt","w")
        file.write("pm")
        file.close()
        return True

def addperson(chat_id, id, password):

    with open("Kakao\people.json", "r+") as file:
        data = json.load(file)
        try:
            del data[chat_id]
        except KeyError:
            pass
        data[chat_id] = {"id":id,"password":password}
        file.seek(0)
        json.dump(data, file)

def readperson(chat_id):
    with open('people.json') as f:
        data = json.load(f)
    return data




class MyClass(client.Client):

    print(1)

    async def onMessage(self, chat):
        print(chat.message)
        print(chat.rawBody)
        print(chat.attachment)



        if chat.message == "/등록":
            await chat.sendText("ksa.hs.kr 아이디와 비밀번호를\n/등록/아이디/비밀번호 형식으로 입력해 주세요")
        
        if chat.message[0:3] == "/등록":
            if chat.message.count("/") == 3:
                id = chat.message.split("/")[2].strip()
                password = chat.message.split("/")[3].strip()
                addperson(chat.authorId,id,password)
                await chat.sendText("등록되었습니다! 작동이 되지 않는다면 다시 등록해주세요")
        

            
# addperson("0","1","2")


# print(check_if_done_am())

client = MyClass("DEVICE")
client.run("10andyye.jongcye@gmail.com", "kakao123@B")
