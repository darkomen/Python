#!/usr/bin/env python
import urllib
import httplib2

http = httplib2.Http()
url = 'https://www.google.com/accounts/ServiceLoginAuth'   
body = {'Email': 'santiago.lopez.pina', 'Passwd': 'goocpdklngle','continue':'http://www.google.com/'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
headers = {'Cookie': response['set-cookie']}
url = 'http://www.google.com/reader/view/#search/kindle//feed%2Fhttp%3A%2F%2Fdevnull.wordpress.com%2Ffeed%2F'   
response, content = http.request(url, 'GET', headers=headers)
print content