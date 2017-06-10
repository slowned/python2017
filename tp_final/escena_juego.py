# -*- encoding: utf-8 -*-
import pilasengine

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.fondos.Galaxia()
        t = self.pilas.actores.Texto(u"Pulsá ESC para regresar")
        t.y = -200
        nave = self.pilas.actores.Nave()
        self.pilas.eventos.pulsa_tecla_escape.conectar(self._regresar)

    def _regresar(self, evento):
        self.pilas.escenas.EscenaMenu()
