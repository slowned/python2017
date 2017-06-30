#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io, os 
import pilasengine
from funciones import es_escena

class HistoriaParser(pilasengine.escena.Escena):

    #cant_historias = 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.secuencia_escenas = []
        self.escenas = {} # {'escNombre':(n,ObjEsc)}
        self.puntaje = 0 
        self.__historia_parser(self.secuencia_escenas)
        self.fin = False

    def __generar_escena(self,scene,line):
        """ Crea escena.txt """

        filename = "cuentos/{0}/{1}.txt".format(self.nombre,scene)
        with open(filename, 'a') as f:
            f.write(line.encode("utf-8"))

    def __nueva_escena(self,line,escenas):
        """ Agrega la escena y devuelve el nombre de la misma"""

        l = line.strip('[').strip(']').replace(' ','').split(',')
        self.secuencia_escenas.append(l[0])
        return l[0]

    def crear_escenas(self):
        n = 0
        for e in self.secuencia_escenas:
            n += 1
            self.escenas[e] = (n,Scene(e))

    def __historia_parser(self,escenas):
        """ Divide la historia en escenas """

        filename = "cuentos/CuentoEjemplo/CuentoEjemplo.txt"
        #filename = 'cuentos/{0}/{1}.txt'.format(self.nombre,self.nombre)
        history = io.open(filename, "r", encoding="utf-8")
        lines = history.readlines()
        history.close()

        for line in lines:
            if es_escena(line[0]):
                scene = self.__nueva_escena(line,escenas)
            self.__generar_escena(scene,line)

    def set_puntaje(self,puntaje):
        self.puntaje += puntaje
        
    def get_puntaje(self):
        return self.puntaje

