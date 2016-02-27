#!/usr/bin/env python3
# Script para descargar todas las tiras cómicas de xkcd

import requests
import random
from bs4 import BeautifulSoup

url = 'http://xkcd.com/archive/'
home = 'http://xkcd.com'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
link = soup.find('div', id='middleContainer')
names = link.find_all('a')

for name in names:
    strip_url = (home+name['href'])
    response = requests.get(strip_url)
    soup = BeautifulSoup(response.content, 'lxml')
    div_img = soup.find('div', id='comic')
    img = div_img.find('img')
    try:
        link_img = "http:" + img['src']
        file_img = './xkcd-en/' + str(img['alt']).replace(' ','') + '.png'
        response = requests.get(link_img)
        file = open(str(file_img), 'wb')
        file.write(response.content)
        file.close()
    except:
        pass

