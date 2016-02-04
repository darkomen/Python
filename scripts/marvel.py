#!/usr/bin/env python3
# Script para descargar todas los nombres de los superheroes marvel
# y elegir de forma aleatoria 4

import requests
import random
from bs4 import BeautifulSoup

url =  'http://marvel.com/comics/characters'

response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
names = soup.select('.az-list a')
super_heroes = [name.text for name in names]

for i in range(4):
	print(super_heroes[random.randint(0,len(super_heroes))])
