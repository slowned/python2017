#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pilasengine, random, os


def guardo_dialogo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    arch = actor+'.txt'
    with open(arch, 'a') as f:
        f.write(dialogo)
    f.close()

guion = open('guion.txt')
#print list(guion)
secuencia_dialogo = []
cant_actores = set(secuencia_dialogo)
# Genero secuencia y linieas de cada actor
for dialogo in guion:
    d = dialogo.split(':')
    secuencia_dialogo.append(d[0])
    guardo_dialogo_actor(d[0],d[1])





# lee linea del actor
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

