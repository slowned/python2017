#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import random
import pilasengine
from crear_actor import ActorPelicula
from pattern.es import conjugate, split, singularize, parse, INFINITIVE
import codecs
import json

pilas = pilasengine.iniciar()
def modifica_linea(dialogo):
    p = parse(dialogo)
    lista = p.split(' ') 
    for i in lista:
	palabra = i.split('/')
        if palabra[1] == 'VB':
	    p = conjugate(palabra[0], INFINITIVE)


def archivo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    d = dialogo.strip()
    act = actor.replace(' ','')
    data = act+".json"
    f = open(data, "a")
    json.dump(d, f)
    f.close()

def generar_guion(actor):
#lee el archivo del  actor actor+'txt' y genera una lista con las lineas
    dialogo = []
    archivo_actor = actor+".json"
    with open(archivo_actor, "r") as f:
        d = str(f.readlines())

    lineas = d[0].split("\"")	
    for linea in lineas:
        dialogo.append(linea)

    return dialogo
	

def random_pos():
    posxy = (random.randrange(-100,100),random.randrange(-100,100))
    return posxy

pos = [] 
for i in range(0,10):
    pos.append(random_pos())

""" ------------ se habre el guion-------------"""

guion = open('guion.txt','r')
g = guion.readlines()
actores = {}
secuencia_dialogo = []

# Genero secuencia y linieas de cada actor
for linea in g:
    l = linea.split(':')
    actor = l[0].strip()
    secuencia_dialogo.append(actor)
    dialogo = l[1] 
    archivo_actor(actor,dialogo)

""" ------------ contrato actores --------------"""

papeles = set(secuencia_dialogo)

print("reparto de guiones")
for actor in papeles:
    lineas = generar_guion(actor) # repartimos el guion
    xy = pos[0]
    act = ActorPelicula(pilas,nombre=actor,position=pos,dialogo=lineas)
    actores[act.get_nombre()] = act
#    actores[actor.get_nombre()] = actor.get_lineas()
    pos.remove(xy)

#dialogo = pilas.actores.Dialogo()
for actor in secuencia_dialogo:
    a = actores[actor]
    linea = a.get_linea()
#    actor.decir(linea)
    print('actor en escena : '+ a.get_nombre())
    print(linea)
#    dialogo.decir(actor,linea)
    a.eliminar_linea(linea)
    print('termino linea del actor')

#dialogo.comenzar()
    

pilas.ejecutar()
