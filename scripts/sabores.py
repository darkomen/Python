#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from math import ceil

class pypizza():
	def __init__(selft):
		self.__restaurante
		self.__
		pass
	def setcomensales(selft):
		pass
	def getcomensales(selft):
		pass
	def setmenus(selft):
		pass
	def getmenus(selft):
		pass
	def setrestaurantes(selft):
		pass
	def getsabores(selft):
		pass




dicarlo = ['Speciale Carlos', 'Barbacue Carlos', '4 Formaggio', 'Carbonata:',
           'Cabrini', 'Supremazia', 'Vegetale', 'Tropicale', 'Quattro Stagione',
           'Diábola', 'Bambinos', 'Bolognesa', 'Granjera']

telepi = ['Telepizza Burger', 'Telepizza Nachos', 'A tu gusto', 'La Ibérica',
          'Pizza Barbacoa', 'Pizza Carbonara', 'Pizza Calzzone Bacon',
          'Pizza Steak House', 'Pizza Bacon Cheeseburger',
          'Pizza Tejana con Cebolla', 'Pizza Tejana', 'Pizza Bacon Crispy',
          'Pizza Chicken Fan Barbacoa', 'Pizza Barbacoa Crème Queso',
          'Pizza Barbacoa Crème Tomate', 'Especial de la casa cebolla',
          'Pizza Calzzone Clásica', 'Especial de la casa champiñón',
          'Pizza Jalisco', 'Pizza Wok', 'Pizza Hot Dog', 'Telepizza Supreme',
          'Pizza Top Cheese & Chicken', 'Pizza Delicheese',
          'Pizza 4 Quesos', 'Pizza Formaggio', 'Pizza Lasaña Especialidad',
          'Pizza Japonesa', 'Pizza Carbonara Cebolla', 'Pizza Hawaiana',
          'Pizza Calzzone Vegetal', 'Pizza Florentina', 'Pizza de la Huerta',
          'Pizza César Deluxe', 'Nueva Pizza Infantil']

vadepizza = ['Pizza 4 Quesos', 'Pizza Fondue', 'Pizza Vegetal', 'Pizza Picante',
             'Pizza Chicken Fondue', 'Pizza Hawaiana', 'Pizza Boloñesa',
             'Pizza Mediterránea', 'Pizza Granjera', 'Pizza Piamontesa',
             'Pizza Carbonara', 'Pizza House', 'Pizza Mar y Montaña',
             'Pizza Barbacoa', 'Pizza Barbacoa Cremosa', 'Pizza Barbacoa House',
             'Pizza Barbacoa Kebab', 'Pizza Chicago', 'Pizza Boloñesa Cremosa']
hungrys = ['Barbacoa', 'Carbonara', 'Cuatro Quesos', 'Hawaiana', 
           "Especial Hungry's cebolla", "Especial Hungry's champiñón",
           'Barbacoa  Creme', 'Barbacoa Creme Tomate', 'Mediterránea',
           'Hot Dog', 'Hot Chili', 'Carbonara Crunch', 'Bacon Crunch',
           'Cheese and Chicken', 'Texas']

print("¿Donde quieres comer hoy?")
print("1. Va De pizza")
print("2. Pizzeria Carlo")
print("3. Telepizza")
print("4. Hungry's")

restaurante = int(input())

if restaurante == 1:
    carta = vadepizza
elif restaurante == 2:
    carta = dicarlo
elif restaurante == 3:
    carta = telepizza
elif restaurante == 4:
    carta = hungrys
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
    # print(carta[int(random.random() * len(carta))])
    print(carta.pop(int(random.random() * len(carta))))
