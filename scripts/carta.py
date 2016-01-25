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
""" Telepizza"""
with urllib.request.urlopen("http://www.telepizza.es/productos/pizzas") as url:
    s = url.read()
bs = BeautifulSoup(s,'lxml')

primary = bs.find_all('div', class_='content_with_highlighted_sidebar wrapper row')
#mod_product_list
#content_with_highlighted_sidebar wrapper row
links = primary[0].find_all('img',class_='productImage')
for i, elements in enumerate(links):
	print((elements.get('title')))	



