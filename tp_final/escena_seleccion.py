# -*- encoding: utf-8 -*-
import pilasengine
from os import listdir
import os

class ElejirHistoria(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.fondos.Tarde()
        t = self.pilas.actores.Texto(u"LISTADO DE HISTORIAS")
        t.y = +200
        #self.imprimir_historias()
        self.pilas.eventos.pulsa_tecla_escape.conectar(self._regresar)

    def _regresar(self, evento):
        self.pilas.escenas.EscenaMenu()

    def imprimir_historias(self):
        path = '/home/slowned/UNLP/python2017/'
        file = listdir

        for f in file:
            print(f)
