#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from historiaParser import HistoryParser
from escena import Scene
from crear_actor import ActorPelicula

h = HistoryParser()
s = Scene()

papeles = set(h.secuencia())

for actor in papeles:
    xy = pos[0]
    lineas = actor_dialogo[actor] 
    act = ActorPelicula(pilas,nombre=actor,position=pos,dialogo=lineas)
    actores[act.get_nombre()] = act
    pos.remove(xy)


