from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import json
import pymongo
import redis
#from pymongo import Connection

#mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["bitcoindata"]

#redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def parse():  
	#data terughalen uit redis
	data = r.get('key1')
	result = json.loads(data)


	jjj = json.dumps(result, indent=2) #van list naar json omvormen
	df = pd.read_json(jjj) #naar dataframe
	df = df.head(1) #enkel de grootste

	ad = df['adres']
	ti = df['tijd']
	bt = df['btc amount']
	do = df['dollar_amount']

	mydict = { "adres": ad.item(), "tijd": ti.item(), "btc amount": bt.item(), "dollar_amount": do.item()} #naar dictionary omvormen
	#print(mydict)
	x = mycol.insert_one(mydict) #inserten in mongodb
	
	print(mydict)

while True:
    time.sleep(60)
    parse()



