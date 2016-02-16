#!/usr/bin/env python3
# Script para descargar todas las tiras cómicas de xkcd

import requests
import random
from bs4 import BeautifulSoup

url = 'http://es.xkcd.com/archive/'
home = 'http://es.xkcd.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
link = soup.find('div', id='archive-ul')
names = link.find_all('a')

for name in names:
    print("#############")
    strip_url = (home+name['href'][3:])
    response = requests.get(strip_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find('img', class_='strip')
    try:
        link_img = home + img['src'][6:]
        file_img = './xkcd/' + str(img['alt']) + '.png'
        file_img = file_img.replace(':', '_')
    except TypeError:
        pass
    print(link_img)
    print(file_img)
    response = requests.get(link_img)
    file = open(str(file_img), 'wb')
    file.write(response.content)
    file.close()
