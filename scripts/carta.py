#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
url_menus={
    'carlos' : 'http://pizzeriascarlos.com/nuestracarta.html',
    'telepizza' : 'http://www.telepizza.es/productos/pizzas',
    'vadepizza' : 'https://www.just-eat.es/restaurants-vadepizzarivas/menu',
    'hungrys' : 'http://www.hungrys.co/pizzas.html'}

carta_carlos = []
carta_telepizza = []
carta_vadepizza = []
carta_hungrys = []
def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html')
        return soup
    else:
        return False

def get_pizzas():
    global carta_carlos
    global carta_telepizza
    global carta_vadepizza
    global carta_hungrys
    # obteniendo menus de Di Carlo
    carlos = get_soup(url_menus['carlos'])
    pizzas = carlos.select('div a[href^=indexpizza_files]')
    carta_carlos = [pizza['title'] for pizza in pizzas]

    # obteniendo menus de Telepizza
    telepizza = get_soup(url_menus['telepizza'])
    pizzas = telepizza.select('div a[class^=styleTitle]')
    carta_telepizza = [pizza.get_text() for pizza in pizzas]

    # obteniendo menus de Hungrys
    hungrys = get_soup(url_menus['hungrys'])
    pizzas = hungrys.select('div.col-md-12 span[class^=thumb-info-inner]')
    carta_hungrys = [pizza.get_text() for pizza in pizzas]

    # obteniendo menus de Vadepizza
    vadepizza = get_soup(url_menus['vadepizza'])
    pizzas = vadepizza.select('h4.product-title')
    pizza = [pizza.get_text().strip() for pizza in pizzas]
    for i,element  in enumerate(pizza):
        if (element.startswith('Pizza')):
            carta_vadepizza.append(element)

get_pizzas()
print("Carta Carlos")
print(carta_carlos)
print("Carta Telepizza")
print(carta_telepizza)
print("Carta Vadepizza")
print(carta_vadepizza)
print("Carta Hungrys")
print(carta_hungrys)
