'''
Author: Gerardathletics

This script gets the most extreme values (maximum temperature, minimum temperature, wind gust and precipitation)
in Spain from Aemet from the previous day. 
The text the bot sends is in spanish.

'''

import requests
from bs4 import BeautifulSoup
import re
from config import *
from datetime import datetime, timedelta

url = 'http://www.aemet.es/ca/eltiempo/observacion/ultimosdatos?k=esp&w=2&datos=img'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# find raw text
find_maxTemp = str(soup.findAll('td')[0:4])
find_minTemp = str(soup.findAll('td')[40:44])
find_wind = str(soup.findAll('td')[120:124])
find_pp = str(soup.findAll('td')[160:163])

# clean the raw text with regex
def clean_text(text):
    cleantext = re.sub('<[^>]+>', '', text).replace('\n', '').replace('\t', '').replace('\r', '').replace('[','').replace(']','')
    return cleantext

max_temperature = clean_text(find_maxTemp)
min_temperature = clean_text(find_minTemp)
wind = clean_text(find_wind)
pp = clean_text(find_pp)

# Getting the link of the location to get the coordinates and altitude
def get_link(index):
    step1 = soup.findAll('td')[index]
    step2 = step1.findAll('a')
    for i in step2:
        step3 = i.get('href')
        link = 'http://www.aemet.es/'+step3
        return link

link_maxTemp = get_link(0)
link_minTemp = get_link(40)
link_wind = get_link(120)
link_pp = get_link(160)

# getting the altitude and coordinates of the place

def getinfo(link):
    resp = requests.get(link)
    soupCoord = BeautifulSoup(resp.text, 'html.parser')
    altitude = str(soupCoord.find_all("div", {"class": "notas_tabla"}))
    altitude = re.findall('(?<=Altitud)(.*?)(?=br)', altitude)
    altitude = re.findall('\d\d\d\d|\d\d\d|\d\d|\d', altitude[0])
    altitude = altitude[0]
    coords = str(soupCoord.findAll('abbr'))
    coords = re.findall('"[^>=]+"', coords)
    coords = ",".join(coords)
    coords = coords.replace('"','').replace('latitude,',' ').replace('longitude,','')
    return altitude, coords

maxTemp_alt, maxTemp_coords = getinfo(link_maxTemp)
minTemp_alt, minTemp_coords = getinfo(link_minTemp)
wind_alt, wind_coords = getinfo(link_wind)
pp_alt, pp_coords = getinfo(link_pp)

# text that will be sent. It includes the meteorological variable, altitude and coordinates.
maxTemp_text = 'TEMP MAX: ' + max_temperature + 'ºC // ' + 'ALT: ' + maxTemp_alt + 'm // LAT,LON: ' + maxTemp_coords
minTemp_text = 'TEMP MIN: ' + min_temperature + 'ºC // ' + 'ALT: ' + minTemp_alt + 'm // LAT,LON: ' + minTemp_coords
wind_text = 'RACHA VIENTO: ' + wind + 'km/h // ' + 'ALT: ' + wind_alt + ' m // LAT,LON: ' + wind_coords
pp_text = 'PRECIPITACION: ' + pp + 'mm // ' + 'ALT: ' + pp_alt + ' m // LAT,LON: ' + pp_coords

# Uncomment below if you want the text printed in the console
# print(maxTemp_text)
# print(minTemp_text)
# print(wind_text)
# print(pp_text)

N_DAYS_AGO = 1
today = datetime.now()
n_days_ago = today - timedelta(days=N_DAYS_AGO)
n_days_ago = str(n_days_ago)
day = 'DIA: ' + n_days_ago[:11]

def send_telegram_message(message):
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
    requests.get(url_req)

send_telegram_message(day)
send_telegram_message(maxTemp_text)
send_telegram_message(minTemp_text)
send_telegram_message(wind_text)
send_telegram_message(pp_text)

