#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request


def main():
    for i in range(10):
        str = "https://static.lwn.net/images/pdf/LDD3/ch18.pdf"
        download_file("https://static.lwn.net/images/pdf/LDD3/ch18.pdf")


def download_file(download_url):
    response = urllib.request.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()
