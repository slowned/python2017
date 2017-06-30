#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from historiaParser import HistoriaParser
from escenaParser import Scene
from crear_actor import ActorPelicula
import pilasengine

pilas = pilasengine.iniciar()

#def contar_historia(historia):
#        s = Scene(escena)
#        s.reproducir()

class CuentosPersonalizado(HistoriaParser):

    def iniciar(self,cuento):
        super(CuentosPersonalizado, self).__init__(cuento)
        self.secuencia_escenas[0][1].reproducir()

    def ejecutar(self):
        pass
    def actualizar(self):
        pass

pilas.ejecutar()
