#!/usr/bin/env python3
# Script para descargar todas los nombres de los superheroes marvel
# y elegir de forma aleatoria 4

import requests
import random
from bs4 import BeautifulSoup

url = 'http://bugmenot.com/view/123dapp.com'

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
names = soup.select('article.account dl kbd')

print((names))
