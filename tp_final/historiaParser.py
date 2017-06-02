# -*- coding: utf-8 -*-

import io, os

class HistoriParser(object):

    self.cantidad = ''

    def __init__(self, nombre):
        self.nombre = nombre
        self.escenas = []
        self.__historia_parser(self.escenas)
        self.puntaje = ''

    def __guardar_escena(self,scene,line):
        # Genera Escena.txt  
        filename = "{0}.txt".format(scene)
        with open(filename, 'a') as f:
            f.write(line.encode("utf-8"))# + os.linesep)

    def __nueva_escena(self,line,escenas):
        # Rotorna el nombre de la escena [Escena1,escena1.txt] >> "Escena1"
        l = line.strip('[').strip(']').replace(' ','').split(',')
        escenas.append(l[0])
        return l[0]

    def __historia_parser(self,escenas):
        """ Divide la historia en escenas """

        history = io.open('historia.txt', "r", encoding="utf-8")
        lines = history.readlines()
        history.close()

        for line in lines:
            if (line[0] == '['):
                scene = self.__nueva_escena(line,escenas)
            self.__guardar_escena(scene,line)

    def set_puntaje(self,puntaje):
        pass

    def get_puntaje(self):
        return self.puntaje

