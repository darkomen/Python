#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
sabores = ['cuatro quesos','fondue','vegetal','picante','CF',
'H','bologñesa','med','granjera','piamontesa','carbonara','house',
'barbacoa','barbacoaC', 'bbqH','BBQK','Chikago','Bolognesa cremosa','m&m']
for i in range(3):
    print(sabores[int(random.random()*len(sabores))])