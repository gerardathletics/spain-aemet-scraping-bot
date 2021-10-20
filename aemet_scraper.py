'''
Author: Gerardathletics

This script gets the most extreme values (maximum temperature, minimum temperature, wind gust and precipitation)
in Spain from Aemet from the previous day.

'''


import requests
from bs4 import BeautifulSoup
import re
from config import *


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

# Getting the link of the location to get the coordinates
link_tmaxpre = soup.findAll('td')[0]
link_tminpre = soup.findAll('td')[40]
link_windpre = soup.findAll('td')[120]
link_pppre = soup.findAll('td')[160]

link_tmaxpre = link_tmaxpre.findAll('a')
link_tminpre = link_tminpre.findAll('a')
link_windpre = link_windpre.findAll('a')
link_pppre = link_pppre.findAll('a')

def create_links(part_link):
    for link in part_link:
        link_part1 = link.get('href')
        link_total = 'http://www.aemet.es/'+link_part1
        print(link_total)



for link in link_tmaxpre:
    linktmax1 = link.get('href')
    link_Tmax = 'http://www.aemet.es/'+linktmax1
    print(link_Tmax)

for link in link_tminpre:
    linktmin1 = link.get('href')
    link_Tmin = 'http://www.aemet.es/'+linktmin1
    print(link_Tmin)

for link in link_windpre:
    linktvent1 = link.get('href')
    link_Wind = 'http://www.aemet.es/'+linktvent1
    print(link_Wind)

for link in link_pppre:
    linktpp1 = link.get('href')
    link_Pp = 'http://www.aemet.es/'+linktpp1
    print(link_Pp)

respTmax = requests.get(link_Tmax)
respTmin = requests.get(link_Tmin)
respVent = requests.get(link_Wind)
respPp = requests.get(link_Pp)

soupTmax = BeautifulSoup(respTmax.text, 'html.parser')
soupTmin = BeautifulSoup(respTmin.text, 'html.parser')
soupVent = BeautifulSoup(respVent.text, 'html.parser')
soupPp = BeautifulSoup(respPp.text, 'html.parser')

tmaxalt = str(soupTmax.find_all("div", {"class": "notas_tabla"}))
tmaxalt = re.findall('(?<=Altitud)(.*?)(?=br)', tmaxalt)
tmaxalt = re.findall('\d\d\d\d|\d\d\d|\d\d|\d', tmaxalt[0])
tmaxalt = tmaxalt[0]

tminalt = str(soupTmin.find_all("div", {"class": "notas_tabla"}))
tminalt = re.findall('(?<=Altitud)(.*?)(?=br)', tminalt)
tminalt = re.findall('\d\d\d\d|\d\d\d|\d\d|\d', tminalt[0])
tminalt = tminalt[0]

ventalt = str(soupVent.find_all("div", {"class": "notas_tabla"}))
ventalt = re.findall('(?<=Altitud)(.*?)(?=br)', ventalt)
ventalt = re.findall('\d\d\d\d|\d\d\d|\d\d|\d', ventalt[0])
ventalt = ventalt[0]

ppalt = str(soupPp.find_all("div", {"class": "notas_tabla"}))
ppalt = re.findall('(?<=Altitud)(.*?)(?=br)', ppalt)
ppalt = re.findall('\d\d\d\d|\d\d\d|\d\d|\d', ppalt[0])
ppalt = ppalt[0]

coordTmax = str(soupTmax.findAll('abbr'))
coordTmax = re.findall('"[^>=]+"', coordTmax)
coordTmax = ",".join(coordTmax)
coordTmax = coordTmax.replace('"','').replace('latitude,',' ').replace('longitude,','')

coordTmin = str(soupTmin.findAll('abbr'))
coordTmin = re.findall('"[^>=]+"', coordTmin)
coordTmin = ",".join(coordTmin)
coordTmin = coordTmin.replace('"','').replace('latitude,',' ').replace('longitude,','')

coordVent = str(soupVent.findAll('abbr'))
coordVent = re.findall('"[^>=]+"', coordVent)
coordVent = ",".join(coordVent)
coordVent = coordVent.replace('"','').replace('latitude,',' ').replace('longitude,','')

coordPp = str(soupPp.findAll('abbr'))
coordPp = re.findall('"[^>=]+"', coordPp)
coordPp = ",".join(coordPp)
coordPp = coordPp.replace('"','').replace('latitude,',' ').replace('longitude,','')

tempMax = 'TEMP MAX: ' + max_temperature + ' // ' + 'ALT: ' + tmaxalt + ' // LAT,LON: ' + coordTmax
tempMin = 'TEMP MIN: ' + min_temperature + ' // ' + 'ALT: ' + tminalt + '// LAT,LON: ' + coordTmin
vent = 'RACHA VIENTO: ' + wind + ' // ' + 'ALT: ' + ventalt + ' // LAT,LON: ' + coordVent
pp = 'PRECIPITACION: ' + pp + ' // ' + 'ALT: ' + ppalt + ' // LAT,LON: ' + coordPp

print(tempMax)
print(tempMin)
print(vent)
print(pp)

from datetime import datetime, timedelta

N_DAYS_AGO = 1

today = datetime.now()
n_days_ago = today - timedelta(days=N_DAYS_AGO)
n_days_ago = str(n_days_ago)
dia = 'DIA: ' + n_days_ago[:11]


url_reqdia = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + dia
url_reqtmax = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + tempMax
url_reqtmin = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + tempMin
url_reqvent = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + vent
url_reqpp = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + pp

resultsdia = requests.get(url_reqdia)
resultstmax = requests.get(url_reqtmax)
resultstmin = requests.get(url_reqtmin)
resultsvent = requests.get(url_reqvent)
resultspp = requests.get(url_reqpp)


print(resultsdia.json())
print(resultstmax.json())
print(resultstmin.json())
print(resultsvent.json())
print(resultspp.json())