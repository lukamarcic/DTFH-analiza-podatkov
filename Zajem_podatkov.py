import csv
import json
import re
import requests
from bs4 import BeautifulSoup

stran = requests.get('https://audioboom.com/channels/4954758.rss')

soup = BeautifulSoup(stran.text, 'html.parser')

ime_datoteke = "DTFH.csv"
datoteka = csv.writer(open(ime_datoteke, 'w', newline='', encoding='utf-8'))
datoteka.writerow(['Naslov', 'Spletna povezava', 'Dolžina', 'Datum', 'Eksplicitnost', 'Opis'])

epizode = soup.select("item")
stevec=0
print(stevec)
for epizoda in epizode:
    stevec += 1
    naslov = (str(epizoda.find("title")))[7:-8]
    spletna_povezava = (str((re.findall(r'link/>.*', str(epizoda)))[0]))[6:]
    dolzina = (str(epizoda.find("itunes:duration")))[17: -18]
    datum = (str(epizoda.select_one("pubDate")))[9:-10]
    eksplicitnost = (str(epizoda.find("itunes:explicit")))[17:-18]
    opis = ((str(epizoda.find("description")))[13:-14]).replace("\r", " ").replace("\n", " ")
    datoteka.writerow([naslov, spletna_povezava, dolzina, datum, eksplicitnost, opis])


print(stevec)