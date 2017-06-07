#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io,os
from crear_actor import ActorPelicula
from funciones import es_escena, es_accion, es_desicion
j
"""-------------se crea la escena--------------------"""

class Scene(object):

    escenas = []

    def __init__(self,nombre):
	self.nombre = nombre
        self.actor_dialogos = {} # {'juan':["hola","soy juan"]} 
        self.actores = {} # {'juan':ObjActorPelicula}
        self.secuencia = [] # [juan,jorge,(accion),juan,{desicion}]
	self.__script_parcer()
        self.escenas.append(self)
        self.decision = {}

    def reproducir(self):
        """ Reproduce una escena """

        for elem in self.secuencia:
            try:
                a = self.actores[elem]
                a.decir(a.get_linea())
            except IndexError:
                if es_accion(elem):
                    pilas.avisar("ACCION")
                elif es_decision(elem):
                    pilas.avisar("DECISION")
                else:
                    pilas.avisar("FIN")

    def __script_parcer(self):
        """ Genera la secuencia de acciones y 
        actores con sus dialogos """

        filename = "{0}.txt".format(nombre)
        guion = io.open(filename, "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        for linea in lineas:
            if es_escena(linea[0]):
                self.nombre = self.nombre
	    elif es_accion(linea[0]):
                self.secuencia.append(linea)
	    elif es_desicion(linea[0]):
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

"""----------------Se crean Actores------------------"""
def crear_actores(dic):

        for actor in self.actor_dialogos.keys():
            lineas = actor_dialogos[actor] 
            act = ActorPelicula(pilas,nombre=actor,actor_dialogo=lineas)
            self.actores[act.get_nombre()] = act



















