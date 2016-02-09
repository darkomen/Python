#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


with urllib.request.urlopen("http://www.sslproxies.org/") as url:
    s = url.read()
bs = BeautifulSoup(s, 'lxml')
table = bs.find('table', {'class': 'display fpltable', 'id': 'proxylisttable'})
rows = table.find_all('tr')
results = []
for row in rows:
    table_data = row.find_all('td')
    if table_data:
        results.append([data.get_text() for data in table_data])

with open("proxies.txt", 'w') as f:
    for ip in results:
        f.write("{}:{}\n".format(ip[0], ip[1]))
