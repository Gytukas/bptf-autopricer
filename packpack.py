import requests
import re
from bs4 import BeautifulSoup
item = "https://backpack.tf/classifieds?item=Bedouin%20Bandana&quality=6&tradable=1&craftable=1&australium=-1&killstreak_tier=0"
puslapis = requests.get(item)
soup = BeautifulSoup(puslapis.content, 'html.parser')
for bandymas in soup.find_all('li'):
    if str(bandymas.get('data-listing_name')) == 'None':
        continue
    if str(bandymas.get('data-listing_intent')) == '1':
        print('Parduoda:' +'\n')
        print(str(bandymas.get('data-listing_name')) + ':' + str(bandymas.get('data-listing_price')))
    else :
        print('Perka:' +'\n')
        print(str(bandymas.get('data-listing_name')) + ':' + str(bandymas.get('data-listing_price')))
