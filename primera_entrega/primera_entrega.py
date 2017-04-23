#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import random
import pilasengine
from crear_actor import ActorPelicula
from pattern.es import conjugate, split, singularize, parse, INFINITIVE
import codecs


pilas = pilasengine.iniciar()
def modifica_linea(dialogo):
    p = parse(dialogo)
    lista = p.split(' ') 
    for i in lista:
	palabra = i.split('/')
        if palabra[1] == 'VB':
	    p = conjugate(palabra[0], INFINITIVE)

def guardo_dialogo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    d = str(dialogo.strip())
    print(d)
    print('---------------')
    act = actor.replace(' ', '')
    arch = act+'.txt'
    f = open(arch, 'a')
    f.write(d+'\n')
    #with open(arch, 'a') as f:
    #    f.write(str(d)+'\n')
    f.close()

def generar_dialogo(actor):
#lee el archivo del  actor actor+'txt' y genera una lista con las lineas
    dialogo_actor = []
    act = actor.replace(' ', '')
    arch = act+'.txt'
    f = open(arch,'r')
    for l in f:
#	print('a infinitivo' + l)
        dialogo_actor.append(str(l))
    return dialogo_actor

def random_pos():
    posxy = (random.randrange(-100,100),random.randrange(-100,100))
    return posxy

pos = [] 
for i in range(0,10):
    pos.append(random_pos())

guion = open('guion.txt','r')
actores = {}

secuencia_dialogo = []
# Genero secuencia y linieas de cada actor
for linea in guion:
    d = linea.split(':')
    actor = d[0]
    secuencia_dialogo.append(actor)
    l = d[1] 
    guardo_dialogo_actor(actor,l)

cant_actores = set(secuencia_dialogo)

for act in cant_actores:
    dialogo = generar_dialogo(act)
    xy = pos[0]  
    actor = ActorPelicula(pilas,nombre=act,position=pos,dialogo=dialogo)
    actores[actor.get_nombre()] = actor
#    actores[actor.get_nombre()] = actor.get_lineas()
    pos.remove(xy)

dialogo = pilas.actores.Dialogo()
for a in secuencia_dialogo:
    actor = actores[a]
    print(actor.get_nombre())
    linea = str(actor.get_lineas()[0])
    print(linea)
    dialogo.decir(actor,linea)
    actor.eliminar_linea(linea)

dialogo.comenzar()
    

pilas.ejecutar()
