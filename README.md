• API Kurulumu

http://my.telegram.org adresine gidin ve giriş yapın.
API geliştirme araçlarına tıklayın ve gerekli alanları doldurun.
İstediğiniz uygulama adını girin ve platform olarak "other" seçeneğini seçin.
Uygulama oluşturduktan sonra "api_id" ve "api_hash" değerlerini kopyalayın (setup.py dosyasında kullanılacak).

• Kurulum ve Kullanım

$ pkg install -y git python

$ git clone https://github.com/qAtheon/TeleGram-Scraper.git

$ cd TeleGram-Scraper

Gereksinimleri yükleyin
$ python3 setup.py -i

Yapılandırma dosyasını entegre edin (apiID, apiHASH)
$ python3 setup.py -c

Kullanıcı Verilerini Oluşturma
$ python3 scraper.py

(members.csv varsayılan dosyadır, ismi değiştirdiyseniz o ismi kullanın)
Toplanan verilere toplu SMS gönderme
$ python3 smsbot.py members.csv

Aracı Güncelleme
$ python3 setup.py -u
