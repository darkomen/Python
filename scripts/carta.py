#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

"""
with urllib.request.urlopen("http://pizzeriascarlos.com/nuestracarta.html") as url:
    s = url.read()
bs = BeautifulSoup(s,'lxml')

primary = bs.find_all('div', class_='content group three')
links = primary[0].find_all('a',class_='vlightbox1')
for i, elements in enumerate(links):
	print((elements.get('title')))	

"""
"""
# Telepizza
with urllib.request.urlopen("http://www.telepizza.es/productos/pizzas") as url:
    s = url.read()
bs = BeautifulSoup(s,'lxml')

primary = bs.find_all('div', class_='content_with_highlighted_sidebar wrapper row')
#mod_product_list
#content_with_highlighted_sidebar wrapper row
links = primary[0].find_all('img',class_='productImage')
for i, elements in enumerate(links):
	print((elements.get('title')))	


"""
# Vadepizza

from urllib.request import Request, urlopen

req = Request('https://www.laneveraroja.com/restaurant/n9mu/vadepizza-rivas-centro', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bs = BeautifulSoup(webpage,'lxml')

primary = bs.find_all('article', class_='menu__category')
#print(primary)
#mod_product_list
#content_with_highlighted_sidebar wrapper row
links = primary[0].find_all('div',class_='menu-item__title')
precio = primary[0].find_all('div',class_='menu-item__variation__price ')
#for i, elements in enumerate(links), enumerate(precio):
#	print((elements.get('title')))	
#links = primary[0].find_all('div',class_='menu-item__variation__price ')
#for i, elements in enumerate(links):
#	print((elements.get_text()))	
menus = [elements.get('title') for elements in links ]
precios =[elements.get_text().split('\n') for elements in precio]
for i in range(len(precios)):
	print("{}: {}".format(menus[i],precios[i][1].replace(' ','')))
