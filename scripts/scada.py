#!/usr/bin/env python3
# Script para descargar todas los nombres de los superheroes marvel
# y elegir de forma aleatoria 4

import requests
import random
from bs4 import BeautifulSoup


s = requests.Session()
url = 'http://172.16.16.15:8088/main/web/login?1-1.IFormSubmitListener-signInForm'
url2 = 'http://172.16.16.15:8088'
home = 'http://172.16.16.15:8088/main/web/'
datos = {
    'id9_hf_0': '',
    'login': 'Login',
    'password': 'password',
    'username': 'admin',
}


login = s.post(url, datos)
response2 = s.get(url2)
print(response2)
soup = BeautifulSoup(response2.content, 'html.parser')
#print(soup)
links = soup.find('span', class_='timer')
#links = soup.find('div', id='login-controls')
print(s.cookies)
names = links.find('a')
print(links)
url_reset = home + names['href'][2:]
print(url_reset)
response = s.get(url_reset)
print(response)
print(s.cookies)
