import json
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


stran = requests.get('https://audioboom.com/channels/4954758.rss')

soup = BeautifulSoup(stran.text, 'html.parser')

#Beautiful soup nam naredi seznam epizod
#OPOMBA: nekatere epizode so bile odstranjene/niso objavljene. Vseh objavljenih epizod v času pisanja je 400.
epizode = soup.select("item")


#Dodatna funkcija za odstranitev določenih stvari iz besedila opisa ter seznam stvari,
# ki jih bomo odstranili (večinmao html oznake)
def remove_all(tekst, sez):
    for item in sez:
        tekst = tekst.replace(item, "")
    return tekst

seznam_ods_stvari_opis =    ('\r', '\n', '<![CDATA[', '<strong>', '</strong>', '<br>', '<div>', '</div>', '<a>', '</a>',
                                '<ul>', '</ul>', '<li>', '</li>', '<em>', '</em>', '<a href=', '>', ']]>', )

#Dodatna funkcija za odstranitev indeksov epizod, ki jih je avtor začel vključevati v naslov na neki točki (napačni so)

def lstrip_multiple(n, tekst, sez):
    i = 0
    for i in range(n):
        for item in sez:
            tekst = tekst.lstrip(item)
        i += 1
    return tekst.lstrip()

seznam_ods_znakov_naslov =  ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ' ')


#Za vsako epizodo izluščimo podatke (podatki so pretvorjeni v string, odstranjeni so začetki in konci,saj so tam bile html oznake)
#Edina izjema je spletna povezava, saj beautiful soup zaradi nekega razloga spremeni format in ga potem ne najde
#Pri opisih epizod so dodatno odstranjene html oznake ter nekateri nevidni znaki, saj so povzročali težave

#seznam naslovov
naslovi = []
for epizoda in epizode:
    naslov1 = ((str(epizoda.find("title")))[7:-8])
    naslov = lstrip_multiple(5, naslov1, seznam_ods_znakov_naslov)
    naslovi.append(naslov)

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
    datumi.append ((str(epizoda.select_one("pubDate")))[9:-16])

#seznam eksplicitnosti
eksplicitnosti = []
for epizoda in epizode:
    eksplicitnosti.append ((str(epizoda.find("itunes:explicit")))[17:-18])

#seznam opisov
opisi = []
for epizoda in epizode:
    opis1 = (' '.join(((str(epizoda.find("description")))[13:-14]).split()))
    opis = remove_all(opis1, seznam_ods_stvari_opis)
    opisi.append(opis)

#Sedaj s Pandas naredimo csv datoteko
slovar =    {'naslov' : naslovi, 'povezava' : spletne_povezave, 'dolzina' : dolzine,
            'datum' : datumi, 'eksplicitnost' : eksplicitnosti, 'opis' : opisi}
df = pd.DataFrame(slovar)
df.to_csv('DTFH.csv', index=False)