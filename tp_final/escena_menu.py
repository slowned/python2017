# -*- encoding: utf-8 -*-
import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        self.fondo = self.pilas.fondos.Volley()
        opciones = [
                    ('cuentos', self._seleccionar_cuento),
                    ('opciones', self._opciones),
		    ('salir', self._salir_del_juego)]

        self.menu = self.pilas.actores.Menu(opciones)

    def _seleccionar_cuento(self):
        self.pilas.escenas.Seleccion()

    def _opciones(self):
        self.pilas.escenas.Opciones()

    def _salir_del_juego(self):
        self.pilas.terminar()

