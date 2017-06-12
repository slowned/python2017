#!/usr/bin/env python
# -*- coding: utf-8 -*-


import io, os
from funciones import es_escena

class HistoriaParser(object):

    cant_historias = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.escenas = []
        self.__historia_parser(self.escenas)
        self.puntaje = 0 

    def __generar_escena(self,scene,line):
        """ Crea escena.txt """

        filename = "cuentos/ejemplo/{0}.txt".format(scene)
        with open(filename, 'a') as f:
            f.write(line.encode("utf-8"))# + os.linesep)

    def __nueva_escena(self,line,escenas):
        """ Agrega la escena y devuelve el nombre de la misma"""

        l = line.strip('[').strip(']').replace(' ','').split(',')
        self.escenas.append(l[0])
        return l[0]

    def __historia_parser(self,escenas):
        """ Divide la historia en escenas """

        filename = 'cuentos/ejemplo/{0}.txt'.format(self.nombre)
        history = io.open(filename, "r", encoding="utf-8")
        lines = history.readlines()
        history.close()

        for line in lines:
            if es_escena(line[0]):
                scene = self.__nueva_escena(line,escenas)
            self.__generar_escena(scene,line)

    def crear_escenas(self):
        for e in len(self.escenas):
            Scene(e)

    def set_puntaje(self,puntaje):
        pass

    def get_puntaje(self):
        return self.puntaje



h = HistoriaParser('cuento')
