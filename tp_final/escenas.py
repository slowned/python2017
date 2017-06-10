#!/usr/bin/env python

import pilasengine
import escena_menu
import escena_juego

pilas = pilasengine.iniciar()



class PantallaBienvenida(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = self.pilas.fondos.Volley()
        self.texto = pilas.actores.Texto(mensaje)

    def ejecutar(self):
        pass
    def actualizar(self):
        self.texto.rotacion += 1
    

pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_juego.EscenaJuego)

pilas.escenas.EscenaMenu()




pilas.ejecutar()
