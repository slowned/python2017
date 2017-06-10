# -*- encoding: utf-8 -*-
import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        opciones = [
		    ('iniciar juego', self._iniciar_juego),
                    ('opciones', self._opciones),
		    ('salir', self._salir_del_juego)]

        self.menu = self.pilas.actores.Menu(opciones)

    def _iniciar_juego(self):
        self.pilas.escenas.EscenaJuego()

    def _opciones(self):
        self.pilas.escenas.Opciones()

    def _salir_del_juego(self):
        self.pilas.terminar()

