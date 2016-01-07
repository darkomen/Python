#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scripts para generar un array con distintos n�meros.
# {270,271,272,272}

strs = "{"
inicio = 260
cuantos = 20
separacion = 1

for i in range(cuantos):
    strs = strs+"{}".format(inicio+(i*separacion))+","

print(strs[:-1]+"};")
