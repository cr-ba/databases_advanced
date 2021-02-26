from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
#import json
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["bitcoindata"]



def scrape():
    page = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(page.content, 'html.parser')

    #alle data scrapen en in 'mixed' list zetten
    mixed = []
    My_table = soup.findAll("div",{"class":"sc-6nt7oh-0 PtIAf"})
    for element in My_table:
      mixed.append(element.text)
      #print(element.text)


    #alle data uit 'mixed' list onderverdelen in juiste categorie
    tijd = []
    btc = []
    dollar_amount = []
    adres = []
    for el in mixed:
        if ":" in el:
            tijd.append(el)
        elif "BTC" in el:
            btc.append(el)
        elif "$" in el:
            newstr = el.replace("$","")
            newstr2 = newstr.replace(",","") #komma en dollar eruitfilteren 
            newfloat = float(newstr2)       #dollarbedrag wordt float ipv string
            dollar_amount.append(newfloat)
        else:
            adres.append(el)

    #lists naar dataframe zetten en row met hoogste dollar_amount printen
    df = pd.DataFrame({'adres':adres, 'tijd':tijd, 'btc amount':btc, 'dollar_amount':dollar_amount})
    final_df = df.sort_values(by=['dollar_amount'], ascending=False)
    #print(final_df.head(1))
    final_df = final_df.head(1)
    #hoogste waarden (moet nog item() achter)
    ad = final_df['adres']
    ti = final_df['tijd']
    bt = final_df['btc amount']
    do = final_df['dollar_amount']

    #print(ad.item())
    #print(ti.item())
    #print(bt.item())
    #print(do.item())

    mydict = { "adres": ad.item(), "tijd": ti.item(), "btc amount": bt.item(), "dollar_amount": do.item()}
    #print(mydict)
    x = mycol.insert_one(mydict) #inserten in mongodb


    #result = final_df.to_json(orient="records")
    #parsed = json.loads(result)
    #print(json.dumps(parsed, indent=2))

while True:
    time.sleep(60)
    scrape()

