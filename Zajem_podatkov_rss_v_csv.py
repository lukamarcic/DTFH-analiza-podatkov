import csv
import json
import requests
import re
import pandas

def dobi_podatke(dat):
    podatki = pd.DataFrame
    epizode = dat.html.find("item", first=False)
    for epizoda in kategorije:
        naslov = epizoda.find('title', first=True).text
        link = epizoda.find('link', first=True).text
        dolzina = epizoda.find('itunes:duration', first=True).text
        datum = epizoda.find('pubDate', first=True).text
        opis = epizoda.find('description', first=True).text

        row = {'Naslov': naslov, 'Povezava': link, 'Dolžina': dolzina, 'Datum': datum,  'Opis': opis}
        podatki = podatki.append(row, ignore_index=True)