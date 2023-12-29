# Author: Catalina Manduta
# Description: Web scraping life history variables from: url = 'https://animalia.bio/

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define headers for the requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
# Start a requests Session
session = requests.Session()

# Read the species names from an Excel file
df = pd.read_excel("Species.xlsx")

# Define the base URL of the site to scrape
url = 'https://animalia.bio/'

# Send a request to the site
response = session.get(url, headers=headers)

# Parse the site's content
soup = BeautifulSoup(response.text, 'html.parser')

# Find and print all div elements with class 'tooltip-title'
titles = soup.find_all('div', class_='tooltip-title')
for title in titles:
    print(title.text)

# Read the names of the species in English from an Excel file
df = pd.read_excel("Eng.xlsx")

# Add new columns to the DataFrame for each characteristic to scrape
df['ActivePeriod'] = None
pos_Active_Period = ["Nocturnal", "Cathemeral", "Diurnal", "Crepuscular"]
df["Diet"] = None
pos_Diet = ['Omnivore',"Herbivore", "Carnivore", "Insectivores", "Folivore","Frugivore", "Graminivore", "Granivore"," Nectarivore",
            "Palynivore", "Planktivore", "Scavenger", "Hypercarnivore", "Gumivorous", "Vermivorous", "Piscivores","Lignivore",
            "Sanguivore", "Molluscivore","Myrmecophagous", "Coprophage", "Mycophage", "Detritivore"]
df["Habitat"] = None
pos_Habitat = ['Terrestrial','Semiaquatic','Burrowing','Arboreal','Fossorial', 'Aquatic']
df["Feeding"] = None
pos_Feeding = ['Predator','Apex predator','Mesopredator','Ambush predator','Pursuit predator', 'Pack hunters','Grazing','Browsing']
df["Locomotion"] = None
pos_Locomotion = ['Cursorial','Jumping','Gliding','Natatorial','Scansorial']
df["Territorial"] = None
pos_Territorial = ['Territorial']
df["MatingBehaviour"] = None
pos_mating =['Monogamy', 'Polygamy', 'Polygyny', 'Polyandry', 'Polygynandry', 'Serial monogamy', 'Cooperative breeder']
df["SeasonalBehaviour"] = None
pos_seasonal_beh = ['Not a migrant', 'Migrating', 'Hibernating', 'Aestivation', 'Altitudinal Migrant', 'Partial Migrant']
df["SocialBehaviour"] = None
pos_social_beh = ['Generally solitary', 'Flocking', 'Solitary', 'Herding', 'Social', 'Highly social', 'Colonial', 'Dominance hierarchy']

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        # Start a new requests Session
        session = requests.Session()
        # Form the URL for each species
        name = row['name engl.']
        name = "-".join(name.split())
        url = 'https://animalia.bio/'
        url_new = url+name+"/"
        print(url_new)
        response = session.get(url_new, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all div elements with class 'tooltip-title'
        titles = soup.find_all('div', class_='tooltip-title')
        # For each tooltip title, check if it matches any of the possible values
        # If it does, add it to the corresponding column in the DataFrame
        for title in titles:
            print(title.text)
            if title.text in pos_Active_Period:
                if pd.isnull(df.at[index, 'ActivePeriod']):
                    df.at[index,'ActivePeriod'] = title.text
                else:
                    df.at[index, 'ActivePeriod'] += ',' + title.text
            if title.text in pos_Diet:
                if pd.isnull(df.at[index, "Diet"]):
                    df.at[index,"Diet"] = title.text
                else:
                    df.at[index, "Diet"] += ',' + title.text
            if title.text in pos_Habitat:
                if pd.isnull(df.at[index, "Habitat"]):
                    df.at[index,"Habitat"] = title.text
                else:
                    df.at[index, "Habitat"] += ',' + title.text
            if title.text in pos_Feeding:
                if pd.isnull(df.at[index, "Feeding"]):
                    df.at[index,"Feeding"] = title.text
                else:
                    df.at[index, "Feeding"] += ',' + title.text
            if title.text in pos_Locomotion:
                if pd.isnull(df.at[index, "Locomotion"]):
                    df.at[index, "Locomotion"] = title.text
                else:
                    df.at[index, "Locomotion"] += ',' + title.text
            if title.text in pos_Territorial:
                if pd.isnull(df.at[index, "Territorial"]):
                    df.at[index, "Territorial"] = title.text
                else:
                    df.at[index, "Territorial"] += ',' + title.text
            if title.text in pos_mating:
                if pd.isnull(df.at[index, "MatingBehaviour"]):
                    df.at[index,"Mating behaviour"] = title.text
                else:
                    df.at[index, "MatingBehaviour"] += ',' + title.text
            if title.text in pos_seasonal_beh:
                if pd.isnull(df.at[index, "SeasonalBehaviour"]):
                    df.at[index,"SeasonalBehaviour"] = title.text
                else:
                    df.at[index, "SeasonalBehaviour"] += ',' + title.text
            if title.text in pos_social_beh:
                if pd.isnull(df.at[index, "SocialBehaviour"]):
                    df.at[index,"SocialBehaviour"] = title.text
                else:
                    df.at[index, "SocialBehaviour"] += ',' + title.text
            else:
                pass
        # Save the DataFrame to an Excel file
        df.to_excel("Species_total2.xlsx", index=False)
    except TypeError as TP:
        print(TP)
        continue
