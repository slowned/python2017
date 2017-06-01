#!/usr/bin/env python
# -*- coding: utf-8 -*-

from historiaParser import HistoryParser
import io,os
"""-------------se crea la escena--------------------"""

class Scene(HistoryParser):
    def __init__(self,nombre):
	self.name = ''
        self.actor_dialogo = {} 
        #self.actores = {} # {'juan':juan}
        self.secuencia = [] # juan, jorge, camina, juan, {desicion}
	self.script_parcer(self.secuencia,self.actor_dialogo,nombre)

    def script_parcer(self,secuencia,actor_dialogo,nombre):
        """ Genera la secuencia de acciones y 
        actores con sus dialogos """

        filename = "{0}.txt".format(nombre)
        guion = io.open(filename, "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        for linea in lineas:
            if linea[0] == '[':
                self.name = self.new_scene(linea)
	    elif linea[0] == '(':
                secuencia.append(linea)
	    elif linea[0] == '{':
                secuencia.append(linea)
	    else:
                l = linea.split(':')
                s = l[1].strip()
                secuencia.append(l[0])
                try:
                    actor_dialogo[l[0]].append(s)
                except(KeyError): 
                    actor_dialogo[l[0]] = []
                    actor_dialogo[l[0]].append(s)

    def secuencia(self):
        return self.secuencia
