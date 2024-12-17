#!/bin/env python3
# kod tarafından : youtube.com/theunknon

"""

Yanlış bir değer girerseniz tekrar setup.py çalıştırabilirsiniz.

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
    os.system('clear')
    print(f"""
{cy}TELEGRAM ÜYE ÇEKİCİ
        {cy}KURULUM
        
    {cy}Sürüm: 1.0
        """)

def requirements():
    def csv_lib():
        banner()
        print(gr+'['+cy+'+'+gr+']'+cy+' bu işlem biraz zaman alabilir...')
        os.system("""
            pip3 install cython numpy pandas
            python3 -m pip install cython numpy pandas
            """)
    banner()
    print(gr+'['+cy+'+'+gr+']'+cy+' csv birleştirme işlemi için 10 dakika kadar sürebilir.')
    input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' csv birleştirmeyi etkinleştirmek ister misiniz? (y/n): ').lower()
    if input_csv == "y":
        csv_lib()
    else:
        pass
    print(gr+"[+] Gereksinimler yükleniyor...")
    os.system("""
        pip3 install telethon requests configparser
        python3 -m pip install telethon requests configparser
        touch config.data
        """)
    banner()
    print(gr+"[+] Gereksinimler başarıyla yüklendi.\n")


def config_setup():
    import configparser
    banner()
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    xid = input(gr+"[+] API ID girin: "+re)
    cpass.set('cred', 'id', xid)
    xhash = input(gr+"[+] Hash ID girin: "+re)
    cpass.set('cred', 'hash', xhash)
    xphone = input(gr+"[+] Telefon numarasını girin: "+re)
    cpass.set('cred', 'phone', xphone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print(gr+"[+] Kurulum tamamlandı!")

def merge_csv():
    import pandas as pd
    import sys
    banner()
    file1 = pd.read_csv(sys.argv[2])
    file2 = pd.read_csv(sys.argv[3])
    print(gr+'['+cy+'+'+gr+']'+cy+' '+sys.argv[2]+' ve '+sys.argv[3]+' dosyaları birleştiriliyor...')
    print(gr+'['+cy+'+'+gr+']'+cy+' Büyük dosyalar zaman alabilir...')
    merge = file1.merge(file2, on='username')
    merge.to_csv("output.csv", index=False)
    print(gr+'['+cy+'+'+gr+']'+cy+' "output.csv" olarak kaydedildi.\n')

def update_tool():
    import requests as r
    banner()
    source = r.get("https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/.image/.version")
    if source.text == '3':
        print(gr+'['+cy+'+'+gr+']'+cy+' Zaten en son sürümde.')
    else:
        print(gr+'['+cy+'+'+gr+']'+cy+' Eski dosyalar kaldırılıyor...')
        os.system('rm *.py'); time.sleep(3)
        print(gr+'['+cy+'+'+gr+']'+cy+' En son dosyalar alınıyor...')
        os.system("""
            curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/add2group.py
            curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/scraper.py
            curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/setup.py
            curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/smsbot.py
            chmod 777 *.py
            """); time.sleep(3)
        print(gr+'\n['+cy+'+'+gr+']'+cy+' Güncelleme tamamlandı.\n')

try:
    if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
        print(gr+'['+cy+'+'+gr+']'+cy+' Seçilen modül : '+re+sys.argv[1])
        config_setup()
    elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
        print(gr+'['+cy+'+'+gr+']'+cy+' Seçilen modül : '+re+sys.argv[1])
        merge_csv()
    elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
        print(gr+'['+cy+'+'+gr+']'+cy+' Seçilen modül : '+re+sys.argv[1])
        update_tool()
    elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
        requirements()
    elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
        banner()
        print("""$ python3 setup.py -m file1.csv file2.csv
            
    ( --config  / -c ) API yapılandırmasını kurar
    ( --merge   / -m ) 2 .csv dosyasını birleştirir
    ( --update  / -u ) Araçları en son sürüme günceller
    ( --install / -i ) Gereksinimleri yükler
    ( --help    / -h ) Bu mesajı gösterir
            """)
    else:
        print('\n'+gr+'['+re+'!'+gr+']'+cy+' Tanınmayan argüman : '+ sys.argv[1])
        print(gr+'['+re+'!'+gr+']'+cy+' Yardım için : ')
        print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
    print('\n'+gr+'['+re+'!'+gr+']'+cy+' Hiçbir argüman verilmedi : '+ sys.argv[1])
    print(gr+'['+re+'!'+gr+']'+cy+' Yardım için : ')
    print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use')
    print(gr+'$ python3 setup.py -h'+'\n')
