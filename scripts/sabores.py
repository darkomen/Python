#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from math import ceil

vadepizza = ['Cuatro Quesos', 'Fondue', 'Vegetal', 'Picante', 'Chicken Fondue',
             'Hawaiana', 'Boloñesa', 'Mediterranea', 'Piamontesa',
             'Carbonara con cebolla','Carbonara con queso', 'House', 'Barbacoa', 'Barbacoa Cremosa', 'Barbacoa House',
             'Barbacoa Kebab', 'Chicago con maiz', 'Chicago con cheddar', 'Bolognesa cremosa', 'Mar y Montaña']

dicarlo = ['Especiale Carlos', 'Cabrini', 'Diabola', 'Barbacue Carlos', 'Supremazia',
           'Bambino', 'Quattro Formaggio', 'Vegetale', 'Bolognesa', 'Carbonata',
           'Tropicale', 'Granjera', 'Quattro Stagione']

print("¿Donde quieres comer hoy?")
print("1. Va De pizza")
print("2. Pizzeria Carlo")

restaurante = int(input())

if restaurante == 1:
    carta = vadepizza
elif restaurante == 2:
    carta = dicarlo
else:
    print("Restaurante no encontrado")
    exit()
comensales = int(input("¿Cuantos comensales somos? "))
hambre = str(input("¿Está Marcial? [y][n]: "))

if hambre.lower() == 'y':
    pizzas = ceil(comensales / 2)
else:
    pizzas = ceil(comensales - 1 / 2)

print("Número de pizzas a pedir: ", pizzas)
for i in range(pizzas):
    #print(carta[int(random.random() * len(carta))])
    print(carta.pop(int(random.random() * len(carta))))
