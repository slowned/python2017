#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io,os,pilasengine
from crear_actor import ActorPelicula
from funciones import es_escena, es_accion, es_decision
"""-------------se crea la escena--------------------"""
pilas = pilasengine.iniciar()

class Scene(pilasengine.escenas.Escena):

    escenas = []

    def iniciar(self,nombre):
	self.nombre = nombre
        self.imagen = ''
        self.actor_dialogos = {} # {'juan':["hola","soy juan"]} 
        self.secuencia = [] # [juan,jorge,(accion),juan,{desicion}]
        self.decision = []
        self.actores = {} # {'juan':ObjActorPelicula}
	self.__script_parcer()
        self.escenas.append(self)

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

    def crear_actores(self):

        for actor in self.actor_dialogos.keys():
            lineas = self.actor_dialogos[actor] 
            act = ActorPelicula(pilas,nombre=actor,dialogo=lineas)
            self.actores[act.get_nombre()] = act

    def __script_parcer(self):
        """ Genera la secuencia de acciones y 
        actores con sus dialogos """

        filename = "cuentos/ejemplo/{0}.txt".format(self.nombre)
        guion = io.open(filename, "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        for linea in lineas:

            if es_escena(linea[0]):
                l = linea.strip('[').replace(']','').replace(' ','').split(',')
                self.nombre = l[0]
                self.imagen = pilas.imagenes.cargar('/home/slowned/UNLP/python2017/python2017/tp_final/fondo1.png')

	    elif es_accion(linea[0]):
                self.secuencia.append(linea)
	    elif es_decision(linea[0]):
                self.secuencia.append(linea)
                d = linea.split(':')
                dl = d[1].split(';')
                self.decision.append(d[0])
                for d in dl:
                    self.decision.append(d)
	    else:
                l = linea.split(':')
                s = l[1].strip()
                self.secuencia.append(l[0])
                try:
                    self.actor_dialogos[l[0]].append(s)
                except(KeyError): 
                    self.actor_dialogos[l[0]] = []
                    self.actor_dialogos[l[0]].append(s)
        self.crear_actores()

"""----------------Se crean Actores------------------"""

















