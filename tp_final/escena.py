#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crear_actor import ActorPelicula
import io,os
"""-------------se crea la escena--------------------"""

class Scene(object):

    def __init__(self,nombre):
	self.nombre = nombre
        self.actor_dialogos = {} # {'juan':["hola","soy juan"]} 
        self.actores = {} # {'juan':ObjActorPelicula}
        self.secuencia = [] # ['juan', jorge, camina, juan, {desicion}]
	self.__script_parcer()

    def __script_parcer(self):
        """ Genera la secuencia de acciones y 
        actores con sus actor_dialogos """

        filename = "{0}.txt".format(nombre)
        guion = io.open(filename, "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        for linea in lineas:
            if linea[0] == '[':
                self.nombre = self.nombre
	    elif linea[0] == '(':
                self.secuencia.append(linea)
	    elif linea[0] == '{':
                self.secuencia.append(linea)
	    else:
                l = linea.split(':')
                s = l[1].strip()
                self.secuencia.append(l[0])
                try:
                    self.actor_dialogos[l[0]].append(s)
                except(KeyError): 
                    self.actor_dialogos[l[0]] = []
                    self.actor_dialogos[l[0]].append(s)

        for actor in self.actor_dialogos.keys():
            lineas = actor_dialogos[actor] 
            act = ActorPelicula(pilas,nombre=actor,actor_dialogo=lineas)
            self.actores[act.get_nombre()] = act
