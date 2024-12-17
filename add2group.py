#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os, sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{cy}TELEGRAM ÜYE ÇEKİCİ
          
    {cy}Sürüm: 1.0
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] İlk olarak python3 setup.py'yi çalıştırın !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Kodu girin: '+re))
 
os.system('clear')
banner()
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
i=0
for group in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    i+=1

print(gr+'[+] Üyeleri eklemek için bir grup seçin')
g_index = input(gr+"[+] Bir numara girin: "+re)
target_group=groups[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
print(gr+"[1] Kullanıcı ID'si ile üye ekle\n[2] Kullanıcı adı ile üye ekle")
mode = int(input(gr+"Giriş: "+re)) 
n = 0
 
for user in users:
    n += 1
    if n % 50 == 0:
        time.sleep(1)
        try:
            print ("Ekleme işlemi: {}".format(user['id']))
            if mode == 1:
                if user['username'] == "":
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                sys.exit(re+"[!] Geçersiz Mod Seçildi. Lütfen Tekrar Deneyin.")
            client(InviteToChannelRequest(target_group_entity,[user_to_add]))
            print(gr+"[+] 5-10 saniye bekleniyor...")
            time.sleep(random.randrange(5, 10))
        except PeerFloodError:
            print(re+"[!] Telegram'dan Flood Hatası alındı. \n[!] Script şu an durduruluyor. \n[!] Bir süre sonra tekrar deneyin.")
        except UserPrivacyRestrictedError:
            print(re+"[!] Kullanıcının gizlilik ayarları bunu yapmanıza izin vermiyor. Atlanıyor.")
        except:
            traceback.print_exc()
            print(re+"[!] Beklenmedik Hata")
            continue
