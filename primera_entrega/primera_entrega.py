#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pilasengine, random, os
import json

def guardo_dialogo_actor(actor,dialogo):
    arch = actor+'.txt'
    with open(arch, 'a') as f:
        f.write(dialogo)
    f.close()

guion = open('guion.txt')
#print list(guion)
secuencia_dialogo = []
actores2 = {}


for dialogo in guion:
    d = dialogo.split(':')
    secuencia_dialogo.append(d[0])
    guardo_dialogo_actor(d[0],d[1])

for actor in secuencia_dialogo:
    arch = actor+'.txt'
    f = open(arch, 'rw+')
    print f.readline() 
# cantidad de actoes en la escena referencia para crear actores en pilas
actores = set(secuencia_dialogo)

print len(actores)
#-----------------------------------

# Pos 
#coordenadas = []

#coordenadas.remove(coordenadas[index])
#------------------------------------

