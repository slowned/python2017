# -*- encoding: utf-8 -*-
import pilasengine
from os import listdir
import os

pilas = pilasengine.iniciar()

class Seleccion(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.fondos.Tarde()
        t = self.pilas.actores.Texto(u"LISTADO DE HISTORIAS")
        t.y = +200
        self.pilas.eventos.pulsa_tecla_escape.conectar(self._regresar)

        path = 'cuentos/'
        lista_cuentos = listdir(path)
        cuentos = []

#        opciones = pilas.interfaz.ListaSeleccion(f, cuando_selecciona)
        for cuento in lista_cuentos:
            o = (cuento,pilas.escenas.CuentosPersonalizado(cuento))
            cuentos.append(o)


        self.menu = self.pilas.actores.Menu(cuentos)


    def sinopsis(self):
        self.pilas.escenas.EscenaSinopsis()

    def _regresar(self, evento):
        self.pilas.escenas.EscenaMenu()

    #def cuando_selecciona(opcion_seleccionada):
    #    pilas.avisar("Ha seleccionado la opcion: " + opcion_seleccionada)

    #def imprimir_historias(self):
    #    path = 'cuentos/'
    #    file = listdir(path)

    #    for f in file:
    #        texto = pilas.actores.Texto(f)
    #        texto1 = pilas.actores.TextoInferior(f)
    #        texto1.color = pilas.colores.verde
    #        texto.color = pilas.colores.azul
    #        pilas.avisar(str(f))
    #        print(f)
