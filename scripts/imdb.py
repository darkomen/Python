#!/usr/bin/env python3
# Script para descargar todas las tiras cómicas de xkcd

import requests
import random
from bs4 import BeautifulSoup

url_famous = 'http://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m_3'
url_historic = 'https://es.wikipedia.org/wiki/Los_100'
url_countries = 'http://www.exitoexportador.com/paises2.htm'
url_movies = 'http://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm_7'
url_shows = 'http://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv_4'

def get_famous(url):
    with open('famosos.txt','w') as file:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find_all('td', class_='name')
        for entry in table:
            name = entry.find('a')
            file.write(name.get_text() + '\n')

def get_historic(url):
    with open('historicos.txt','w') as file:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.select('ol li')
        for entry in table:
            name = entry.find('a')
            print(name.get_text())
            file.write(name.get_text() + '\n')

def get_countries(url):
    with open('paises.txt','w') as file:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.select('li')

        for entry in table:
            name = entry.find('a')
            file.write(name.get_text() + '\n')

def get_movies(url):
    with open('peliculas.txt','w') as file:
        response = requests.get(url)
        print(response)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find_all('td', class_='titleColumn')
        #print(table)
        for entry in table:
            name = entry.find('a')
            print(name.get_text())
            file.write(name.get_text() + '\n')

def get_shows(url):
    with open('series.txt','w') as file:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find_all('td', class_='titleColumn')
        for entry in table:
            name = entry.find('a')
            print(name.get_text())
            file.write(name.get_text() + '\n')

def main():
    print('Obteniendo nombres de actores famosos')
    get_famous(url_famous)
    print('Obteniendo nombres de personajes historicos')
    get_historic(url_historic)
    print('Obteniendo nombres de paises del mundo')
    get_countries(url_countries)
    print('Obteniendo nombres de peliculas')
    get_movies(url_movies)
    print('Obteniendo nombres de series')
    get_shows(url_shows)

if __name__ == "__main__":
    main()
