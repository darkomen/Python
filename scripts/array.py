#!/usr/bin/python

# Scripts para generar un array con distintos números.
# {270,271,272,272}

strs="{"
inicio=271
cuantos=20

for i in range(cuantos):
    strs=strs+"{}".format(inicio+i)+","


print(strs[:-1]+"}")
