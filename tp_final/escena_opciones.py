# -*- encoding: utf-8 -*-
import pilasengine

class Opciones(pilasengine.escenas.Escena):

    def iniciar(self):
        t = self.pilas.actores.Texto(u"OPCIONES:")
        t.y = -200
        self.sonido = True #pregunta 
        self.pilas.eventos.pulsa_tecla_escape.conectar(self._regresar)

    def _regresar(self, evento):
        self.pilas.escenas.EscenaMenu()
