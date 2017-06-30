#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#from boton import *
from crear_dialogo import GuionParser
from crear_actor import ActorPelicula
from pattern.es import conjugate, split, singularize, parse, INFINITIVE
import os, io, random, pilasengine

pilas = pilasengine.iniciar()

def hablando(actor, secuencia):
    try:
        a=actor[secuencia[0]]
        actor[secuencia[0]].decir(actor[secuencia[0]].get_linea())
        secuencia.remove(secuencia[0])
    except IndexError:
	pilas.avisar("SE TERMINO LA PELI!!!")

def random_pos():
    posxy = (random.randrange(-100,100),random.randrange(-100,100))
    return posxy

pos = [] 
for i in range(0,10):
    pos.append(random_pos())

def modifica_linea(dialogo):
    p = parse(dialogo)
    lista = p.split(' ') 
    linea = []
    for i in lista:
	palabra = i.split('/')
        if palabra[1] == 'VB':
	    p = conjugate(palabra[0], INFINITIVE)
            linea.append(p)
        elif palabra[1] == 'NN':
	    linea.append(singularize(palabra[0]))
        else:
	    linea.append(palabra[0])
    l = " ".join(linea)
    return l

def guardo_archivo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    act = actor.replace(' ','')
    filename = "{0}.txt".format(act)
    with open(filename, 'a') as f:
        f.write(dialogo.encode("utf-8") + os.linesep)



""" ------------ se habre el guion-------------"""

guion = io.open('guion.txt', "r", encoding="utf-8")
lines = guion.readlines()
guion.close()
actor_dialogo = {}

actores={}
secuencia_dialogo = []

for dialogo in lines:
    l = dialogo.split(':')
    d = l[1].strip()
    dm = modifica_linea(d)
    secuencia_dialogo.append(l[0])
    guardo_archivo_actor(l[0],dm)
    
    try:
	actor_dialogo[l[0]].append(dm)
    except(KeyError): 
	actor_dialogo[l[0]] = []
	actor_dialogo[l[0]].append(dm)

""" ------------ contrato actores --------------"""

papeles = set(secuencia_dialogo)

for actor in papeles:
    xy = pos[0]
    lineas = actor_dialogo[actor] 
    act = ActorPelicula(pilas,nombre=actor,position=pos,dialogo=lineas)
    actores[act.get_nombre()] = act
    pos.remove(xy)


b = pilas.interfaz.Boton("empezar dialogo")
b.y = -125
b.x = 125
b.conectar(lambda : hablando(actores,secuencia_dialogo))
    

pilas.ejecutar()
