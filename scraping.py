from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


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
    print(final_df.head(1))

while True:
    time.sleep(60)
    scrape()

