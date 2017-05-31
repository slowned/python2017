#!/usr/bin/env python
# -*- coding: utf-8 -*-

from historiaParser import HistoryParser

"""-------------se crea la escena--------------------"""

class Scene(object):
    def __init__(self):
	self.name = ''
	self.script_parcer()

    def guion_escenea(self):
        guion = io.open('escena1.txt', "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        actor_dialogo = {}
        actores = {}
        secuencia_dialogo = []

        for linea in lineas:
            if line[0] == '[':
                self.name = HistoryParser.new_scene(line)
	    elif line[0] == '(':
		print 'agreo accion a la lista_secuencia'
	    elif line[0] == '{':
		print 'agrego decicion a lista_secuncia'
	    else:
		print 'agrego actor a lista_secuencia'
		    try:
			actor_dialogo[l[0]].append(dm)
		    except(KeyError): 
			actor_dialogo[l[0]] = []
			actor_dialogo[l[0]].append(dm)

	    	
    
