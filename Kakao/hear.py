import client
from packet import Packet
import bson
import time
import json
import os
import hashlib
import mimetypes
import httpApi

class MyClass(client.Client):

    async def onMessage(self, chat):
        print(chat.message)
        print('################################')
        print(chat.attachment)
        print('################################')
        print(chat.rawBody)


client = MyClass("DEVICE")



client.run("10andyye.jongcye@gmail.com", "kakao123@B")
