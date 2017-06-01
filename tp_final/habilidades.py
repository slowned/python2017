#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pilasengine

class posicionar(pilasengine.habilidades.Habilidad):
    """ Posiciona el actor en las coordenadas (x,y) """ 
    def iniciar(self,actor,posicion):
        self.receptor = actor
        self.x = posicion[0]
        self.y = posicion[1]

    def actualizar(self):
        self.receptor.x = self.x
        self.receptor.y = self.y

class caminar(object):

    def iniciar(self,actor):
        self.receptor = actor

    def actualizar(self):
        self.receptor.x = self.x
        self.receptor.y = self.y

class correr(object):
    pass

class saltar(object):
    pass

class volverse_loco(object):
    pass

class reir(object):
    pass

class seguir_a(object):
    pass

class llorar(object):
    pass

class hablar_infinitivo(object):
    pass

class hablar_normal(object):
    pass

class sonar(object):
    pass



