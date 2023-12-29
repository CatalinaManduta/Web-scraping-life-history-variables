
# Project: Castration in males
# Author: Catalina Manduta
# Description: Web scraping life history variables from: url = 'https://animalia.bio/

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

session = requests.Session()
df = pd.read_excel("Species.xlsx")
url = 'https://animalia.bio/'
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_='tooltip-title')
for title in titles:
    print(title.text)


df = pd.read_excel("Eng.xlsx")
df['Active Day Period'] = None
pos_Active_Period = ["Nocturnal", "Cathemeral", "Diurnal", "Crepuscular"]
df["Diet"] = None
pos_Diet = ['Omnivore',"Herbivore", "Carnivore", "Insectivores", "Folivore","Frugivore", "Graminivore", "Granivore"," Nectarivore",
            "Palynivore", "Planktivore", "Scavenger", "Hypercarnivore", "Gumivorous", "Vermivorous", "Piscivores","Lignivore",
            "Sanguivore", "Molluscivore","Myrmecophagous", "Coprophage", "Mycophage", "Detritivore"]
df["LifeStyle"] = None
pos_LifeStyle = ['Semiaquatic', 'Terrestrial', 'Cursorial', 'Burrowing', 'Arboreal', 'Fossorial', 'Aquatic', 'Jumping', 'Wading birds',
                 'Pelagic birds', 'Gliding', 'Soaring birds', 'Flightless bird', 'Apex predator', 'Mesopredator', 'Predator',
                 'Ambush predator', 'Pursuit predator', 'Grazing', 'Browsing', 'Pack hunters', 'Altricial', 'Precocial',
                 'Waterfowl', 'Zoochory', 'Oviparous', 'Island endemic', 'Scansorial', 'Territorial', 'Viviparous',
                 'Natatorial', 'Congregatory', 'Ovoviviparous', 'Torpor', 'Nomadic', 'Cosmopolitan']
df["Mating behaviour"] = None
pos_mating =['Monogamy', 'Polygamy', 'Polygyny', 'Polyandry', 'Polygynandry', 'Serial monogamy', 'Cooperative breeder']
df["Seasonal behaviour"] = None
pos_seasonal_beh = ['Not a migrant', 'Migrating', 'Hibernating', 'Aestivation', 'Altitudinal Migrant', 'Partial Migrant']
df["Social Behaviour"] = None
pos_socia_beh = ['Generally solitary', 'Flocking', 'Solitary', 'Herding', 'Social', 'Highly social', 'Colonial', 'Dominance hierarchy']
for index, row in df.iterrows():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        session = requests.Session()
        name = row['name engl.']
        name = "-".join(name.split())
        url = 'https://animalia.bio/'
        url_new = url+name+"/"
        print(url_new)
        response = session.get(url_new, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('div', class_='tooltip-title')
        for title in titles:
            print(title.text)
            if title.text in pos_Active_Period:
                if pd.isnull(df.at[index, 'Active Day Period']):
                    df.at[index,'Active Day Period'] = title.text
                else:
                    df.at[index, 'Active Day Period'] += ',' + title.text
            if title.text in pos_Diet:
                if pd.isnull(df.at[index, "Diet"]):
                    df.at[index,"Diet"] = title.text
                else:
                    df.at[index, "Diet"] += ',' + title.text
            if title.text in pos_LifeStyle:
                if pd.isnull(df.at[index, "LifeStyle"]):
                    df.at[index,"LifeStyle"] = title.text
                else:
                    df.at[index, "LifeStyle"] += ',' + title.text
            if title.text in pos_mating:
                if pd.isnull(df.at[index, "Mating behaviour"]):
                    df.at[index,"Mating behaviour"] = title.text
                else:
                    df.at[index, "Mating behaviour"] += ',' + title.text
            if title.text in pos_seasonal_beh:
                if pd.isnull(df.at[index, "Seasonal behaviour"]):
                    df.at[index,"Seasonal behaviour"] = title.text
                else:
                    df.at[index, "Seasonal behaviour"] += ',' + title.text
            if title.text in pos_socia_beh:
                if pd.isnull(df.at[index, "Social Behaviour"]):
                    df.at[index,"Social Behaviour"] = title.text
                else:
                    df.at[index, "Social Behaviour"] += ',' + title.text
            else:
                pass
        df.to_excel("Species_total.xlsx", index=False)
    except TypeError as TP:
        print(TP)
        continue


