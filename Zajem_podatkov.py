import csv
import json
import re
import requests
from bs4 import BeautifulSoup


stran = requests.get('https://audioboom.com/channels/4954758.rss')

soup = BeautifulSoup(stran.text, 'html.parser')

#Beautiful soup nam naredi seznam epizod
epizode = soup.select("item")

podatki_epizod = []

#za vsako epizodo izluščimo podatke (podatki so pretvorjeni v string, odstranjeni so začetki in konci, tam so bile html oznake)
#edina izjema je spletna povezava, saj beautiful soup zaradi nekega razloga spremeni format in ga potem ne najde
for epizoda in epizode:
    naslov = (str(epizoda.find("title")))[7:-8]
    spletna_povezava = (str((re.findall(r'link/>.*', str(epizoda)))[0]))[6:]
    dolzina = (str(epizoda.find("itunes:duration")))[17: -18]
    datum = (str(epizoda.select_one("pubDate")))[9:-10]
    eksplicitnost = (str(epizoda.find("itunes:explicit")))[17:-18]
    opis = ((str(epizoda.find("description")))[13:-14]).replace("\r", " ").replace("\n", " ")
    podatki_epizod.append([naslov,spletna_povezava, dolzina, datum, eksplicitnost, opis])

#seznam epizod sedaj zapišemo v csv datoteko

ime_datoteke = "DTFH.csv"
datoteka = csv.writer(open(ime_datoteke, 'w', newline='', encoding='utf-8'))
datoteka.writerow(['Naslov', 'Spletna povezava', 'Dolžina', 'Datum', 'Eksplicitnost', 'Opis'])
datoteka.writerows(podatki_epizod)
