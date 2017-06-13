#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from historiaParser import HistoriaParser
from escenaParser import Scene
from crear_actor import ActorPelicula
import pilasengine

pilas = pilasengine.iniciar()

def contar_historia(historia):
        s = Scene(escena)
        s.reproducir()


h = HistoriaParser()


contar_historia(h)


pilas.ejecutar()

























#b = pilas.interfaz.Boton("empezar dialogo")
#b.y = -125
#b.x = 125
#
#
#b.conectar(lambda : actuar(s.actores,s.secuencia))


pilas.ejecutar()
