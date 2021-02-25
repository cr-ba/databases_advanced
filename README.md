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

En om het script dan effectief te runnen:
```bash
python3 scraping.py
```

## week 2: Data naar Mongodb sturen

pymongo installeren
```bash
pip3 install pymongo
```
