#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME = 30

class main():

    def banner():
        
        print(f"""
{cy}TELEGRAM ÜYE ÇEKİCİ
          
    {cy}Sürüm: 1.0
        """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] önce python3 setup.py çalıştırın !!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Kodunuzu Girin: '+re))
        
        os.system('clear')
        main.banner()
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
        print(gr+"[1] kullanıcı ID'si ile mesaj gönder\n[2] kullanıcı adı ile mesaj gönder")
        mode = int(input(gr+"Seçim Yapın: "+re))
         
        message = input(gr+"[+] Mesajınızı Girin: "+re)
         
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Geçersiz Mod. Çıkılıyor.")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Mesaj Gönderiliyor:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print(gr+"[+] {} saniye bekleniyor".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(re+"[!] Telegram'dan Flood Hatası alındı. \n[!] Script şu anda duruyor. \n[!] Lütfen biraz sonra tekrar deneyin.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] Hata:", e)
                print(re+"[!] Devam etmeye çalışılıyor...")
                continue
        client.disconnect()
        print("Tamam. Mesaj tüm kullanıcılara gönderildi.")


main.send_sms()
