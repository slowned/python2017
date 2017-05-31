#!/usr/bin/env python
# -*- coding: utf-8 -*-

from historiaParser import HistoryParser

"""-------------se crea la escena--------------------"""

class Scene(object):
    def 

    def guion_escenea(self):
        guion = io.open('escena1.txt', "r", encoding="utf-8")
        lineas = guion.readlines()
        guion.close()

        actor_dialogo = {}
        actores = {}
        secuencia_dialogo = []

        for linea in lineas:
            if (line[0] == '['):
                scene = HistoryParser.new_scene(line)
    
