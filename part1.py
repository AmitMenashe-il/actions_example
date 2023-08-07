import requests
import csv

BASE_URL = "https://rickandmortyapi.com/api"

base_url = requests.get(BASE_URL)

# get characters
char_url = base_url.json()['characters']
characters = requests.get(char_url).json()['results']

# Human Alive Earth list
charsPicked = []
species = 'Human'
status = 'Alive'
origin = 'Earth'

for character in characters:
    if (character['species'] == species and character['status'] == status and character['origin'][
        'name'].startswith(
            'Earth')):
        charsPicked.append(character)

# Name Location Image list

f = open('chars.csv', 'w')
writer = csv.writer(f)

for character in charsPicked:
    writer.writerow([character['name'], character['location'], character['image']])