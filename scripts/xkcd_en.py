#!/usr/bin/env python3
# Script para descargar todas las tiras cómicas de xkcd

import requests
import random
import os
import time
from bs4 import BeautifulSoup

class strip():
    def __init__(self):
        self.__count = 0
        self.__url = 'http://xkcd.com/archive/'
        self.__home = 'http://xkcd.com'
        self.__folder = './xkcd/'
        self.__start_time = 0
        self.__end_time = 0
        self.__elapsed_time = 0
        if not os.path.exists(self.__folder):
            os.makedirs(self.__folder)

    def get_soup(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            return False

    def check_file(self, file):
        return os.path.exists(file):

    def main(self):
        self.__start_time = time.time()
        soup = self.get_soup(self.__url)
        link = soup.find('div', id='middleContainer')
        names = link.find_all('a')

        for name in names:
            strip_url = self.__home + name['href']
            soup = self.get_soup(strip_url)
            div_img = soup.find('div', id='comic')
            img = div_img.find('img')

            try:
                link_img = "http:" + img['src']
                file_img = self.__folder + str(img['alt']).replace(' ','') + '.png'
                if self.check_file(file_img):
                    print("fichero existe")
                    pass
                else:
                    response = requests.get(link_img)
                    file = open(str(file_img), 'wb')
                    file.write(response.content)
                    file.close()
                    print("Tira cómica salvada en: {}".format(file_img))
                    self.__count = self.__count + 1
            except:
                print("Se ha producido un error al acceder a la tira")
                pass

        self.__end_time = time.time()
        self.__elapsed_time = self.__end_time - self.__start_time
        print("Descargadas un total de {} tiras de {} en {} s".format(self.__count, self.__home, self.__end_time))

if __name__ == '__main__':
    xkcd = strip()
    xkcd.main()
