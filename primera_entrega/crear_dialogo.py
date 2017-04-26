#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pilasengine, random, os


def guardo_archivo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    d = dialogo.strip()
    act = actor.replace(' ','')
    arch = act+'.txt'
    with open(arch, 'a') as f:
        f.write(d+"\n")
    f.close()

guion = open('guion.txt','r')
lines = guion.readlines()
#print list(guion)
secuencia_dialogo = []
# Genero secuencia y linieas de cada actor
actor_dialogo = {}
for dialogo in lines:
    l = dialogo.split(':')
    print(l[1])
    secuencia_dialogo.append(l[0])
    guardo_archivo_actor(l[0],l[1])
    
    try:
	actor_dialogo[l[0]].append(l[1])
    except(KeyError): 
	actor_dialogo[l[0]] = []
	actor_dialogo[l[0]].append(l[1])


for v in actor_dialogo.values():
    print(v)

## lee linea del actor
#for actor in secuencia_dialogo:
#    arch = actor+'.txt'
#    f = open(arch, 'rw+')
#    print f.readline() 
## cantidad de actoes en la escena referencia para crear actores en pilas
actores = set(secuencia_dialogo)

print len(actores)
#-----------------------------------

# Pos 
#coordenadas = []

#coordenadas.remove(coordenadas[index])
#------------------------------------

