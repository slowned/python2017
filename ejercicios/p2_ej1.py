#!/usr/bin/env python

import random

colores = ['azul', 'amarillo', 'rojo', 'blanco', 'negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

dic = {}

for c in coordenadas:
    color_index = random.randint(0,len(colores)-1)
    dic[c] = colores[color_index]

print ("estructura con colores repetidos:\n" + str(dic))

dic_sin_repetir = {}

for c in coordenadas:
    color_index = random.randint(0,len(colores)-1)
    dic_sin_repetir[c] = colores[color_index]
    colores.remove(colores[color_index])

print ("estructura sin colores repetidos:\n" + str(dic_sin_repetir))
