#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from historiaParser import HistoryParser
from escena import Scene
from crear_actor import ActorPelicula
import pilasengine

pilas = pilasengine.iniciar()

def actuando(actor,secuencia):
    try:
        a=actor[secuencia[0]]
        actor[secuencia[0]].decir(actor[secuencia[0]].get_linea())
        secuencia.remove(secuencia[0])
    except IndexError:
        if es_accion(secuencia[0]):
            pilas.avisar("ACCION")
        elif es_decision(secuendia[0]):
            pilas.avisar("DECISION")
        else:
            pilas.avisar("FIN")

h = HistoryParser()
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
