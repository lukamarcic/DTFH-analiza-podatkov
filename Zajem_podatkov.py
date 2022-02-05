import csv
import json
import re
import requests
from bs4 import BeautifulSoup


stran = requests.get('https://audioboom.com/channels/4954758.rss')

soup = BeautifulSoup(stran.text, 'html.parser')

#Beautiful soup nam naredi seznam epizod
epizode = soup.select("item")


#Dodatna funkcija za zamenjavo
def remove_all(tekst, sez):
    for item in sez:
        tekst = tekst.replace(item, "")
    return tekst

seznam_ods_stvari_opis =    ('\r', '\n', '<![CDATA[', '<strong>', '</strong>', '<br>', '<div>', '</div>', '<a>', '</a>',
                                '<ul>', '</ul>', '<li>', '</li>', '<em>', '</em>', '<a href=', '>', ']]>', )

#Za vsako epizodo izluščimo podatke (podatki so pretvorjeni v string, odstranjeni so začetki in konci,saj so tam bile html oznake)
#Edina izjema je spletna povezava, saj beautiful soup zaradi nekega razloga spremeni format in ga potem ne najde
#Pri opisih epizod so dodatno odstranjene html oznake ter nekateri nevidni znaki, saj so povzročali težave

podatki_epizod = []
for epizoda in epizode:
    naslov = ((str(epizoda.find("title")))[7:-8])
    spletna_povezava = (str((re.findall(r'link/>.*', str(epizoda)))[0]))[6:]
    dolzina = (str(epizoda.find("itunes:duration")))[17: -18]
    datum = (str(epizoda.select_one("pubDate")))[9:-10]
    eksplicitnost = (str(epizoda.find("itunes:explicit")))[17:-18]
    opis1 = (' '.join(((str(epizoda.find("description")))[13:-14]).split()))
    opis = remove_all(opis1, seznam_ods_stvari_opis)
    podatki_epizod.append([naslov, spletna_povezava, dolzina, datum, eksplicitnost, opis])


#seznam epizod sedaj zapišemo v csv datoteko


ime_datoteke = "DTFH.csv"
datoteka = csv.writer(open(ime_datoteke, 'w', newline='', encoding='utf-8'))
datoteka.writerow(['Naslov', 'Spletna povezava', 'Dolžina', 'Datum', 'Eksplicitnost', 'Opis'])
datoteka.writerows(podatki_epizod)









#seznam naslovov
naslovi = []
for epizoda in epizode:
    naslovi.append ((str(epizoda.find("title")))[7:-8])

#seznam spletnih povezav
spletne_povezave = []
for epizoda in epizode:
    spletne_povezave.append ((str((re.findall(r'link/>.*', str(epizoda)))[0]))[6:])

#seznam dolžin
dolzine = []
for epizoda in epizode:
    dolzine.append ((str(epizoda.find("itunes:duration")))[17: -18])

#seznam datumov
datumi = []
for epizoda in epizode:
    datumi.append ((str(epizoda.select_one("pubDate")))[9:-10])

#seznam eksplicitnosti
eksplicitnosti = []
for epizoda in epizode:
    eksplicitnosti.append ((str(epizoda.find("itunes:explicit")))[17:-18])

#seznam opisov
opisi = []
for epizoda in epizode:
    opisi.append (' '.join((((str(epizoda.find("description")))[13:-14]).replace("\r", " ").replace("\n", " ")).split()))