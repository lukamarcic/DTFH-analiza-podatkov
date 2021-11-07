import csv
import json
import requests
import re


vzorec_epizode = re.compile(
    r'<item>.*'

)

vzorec_naslova = re.compile(
    a
)

vzorec_spletnega_naslova = re.compile(

)

vzorec_datuma = re.compile(

)

vzorec_dolzine = re.compile(

)

vzorec_gosta = re.compile(

)

vzorec_opisa = re.compile(

)


def izloci_podatke_podcasta(tekst):
    return None


epizode = []

with open("DTFH.csv", "w") as dat:
    writer = csv.DictWriter(dat, [
        "naslov",
        "spletni naslov",
        "datum",
        "dolzina",
        "gost",
        "opis",
    ])
    writer.writeheader()
    writer.writerows(epizode)