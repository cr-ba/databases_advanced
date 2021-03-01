# databases_advanced

## week 1: scraper op ubuntu VM

Zie dat python 3 is geïnstalleerd op VM (automatisch bij ubuntu).

om te starten in terminal: 
```bash
sudo apt update
```

Om python libraries te installeren zal ik pip3 gebruiken. Installeer alvast pip3 via command line:
```bash
sudo apt install python3-pip
```

installeer alle python libraries die het script nodig heeft via terminal:
```bash
pip3 install bs4
pip3 install requests
pip3 install pandas
```

Scraping.py staat in de documents folder van het VM (in mijn geval toch). Om het script te runnen verander je eerst van directory:
```bash
Cd home/user/Documents
```
of
```bash
cd ~/Documents
```

En om het script dan effectief te runnen:
```bash
python3 scraping.py
```

## week 2: Data naar Mongodb sturen

pymongo installeren
```bash
pip3 install pymongo
```
installeer mongo db (zie slides)

Mongodb starten
```bash
mongo
```
installeer compass
```bash
wget -4 https://downloads.mongodb.com/compass/mongodb-compass_1.25.0_amd64.deb
sudo dpkg -i mongodb-compass_1.25.0_amd64.deb
```
start compass
```bash
mongodb-compass
```

en run tenslotte het nieuwe script scraping_week2.py. Elke minuut wordt de grootste transactie weggeschreven naar mongodb.

## week 3: alle data naar redis, vervolgens met parser data uit redis halen en grootste transactie naar mongodb sturen

installeer redis voor python
```bash
pip3 install redis
```
installeer redis op VM (zie slides)
```bash
wget  http :// download.redis.io/redis -stable.tar.gz
tar  xvzf  redis -stable.tar.gz
cd redis -stable
make
make  test
```
nog een install
```bash
Sudo apt install redis-server
```
redis starten (zie slides)
```bash
Cd redis-stable
cd src
redis -server
```
redis stoppen (hangt af van systeem)
```bash
redis-cli shutdown
```

scraping_week3.py scraped en stuurt alle data door naar redis elke 60 seconden. parser.py haalt elke 60 seonden alle data uit redis en selecteert de data van de grootste transactie, deze data wordt naar mongodb gestuurd.
