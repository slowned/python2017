#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from historiaParser import HistoryParser
from escena import Scene
from crear_actor import ActorPelicula
import pilasengine

pilas = pilasengine.iniciar()

def contar_historia(historia):
    for escena in len(historia.escenas):
        s = Scene(escena)
        actuando(s)


h = HistoryParser()

ss = h.crear_escenas()

s = Scene(h.escena[0])
escenas = []

for i in len(h.escenas):
   escenas.append(Scene(i)) 

"""------main menu---------"""
bg = pilas.imagenes.cargar('imagenes/'+random.choice(os.listdir('imagenes/')))# if imagen else "imagenes/ribbit7-300px.png"


























#b = pilas.interfaz.Boton("empezar dialogo")
#b.y = -125
#b.x = 125
#
#
#b.conectar(lambda : actuar(s.actores,s.secuencia))


pilas.ejecutar()
