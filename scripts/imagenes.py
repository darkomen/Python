#!/usr/bin/env python3
# Script para descargar todas las imagenes de la web
# http://shop.lingvistov.com/catalog/prints/page/

import requests
from bs4 import BeautifulSoup

url = 'http://shop.lingvistov.com/catalog/prints/'
counter = 0

for i in range(6):
    response = requests.get(url + 'page/' + str(i) + '/')
    soup = BeautifulSoup(response.content, 'lxml')
    imgs = soup.select('ul.products img')
    for img in imgs:
        response = requests.get(img['src'])
        file = open(str(img['alt']) + '.png', 'wb')
        file.write(response.content)
        file.close()
        counter += 1

print(("DONE DOwnloads {} Figures".format(counter)))
