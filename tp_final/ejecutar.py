# -*- encoding: utf-8 -*-
import pilasengine

import escena_juego, escena_opciones, escena_menu, escena_seleccion

pilas = pilasengine.iniciar()


# Vinculamos las escenas

pilas.escenas.vincular(escena_seleccion.ElejirHistoria)
pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_juego.EscenaJuego)
pilas.escenas.vincular(escena_opciones.Opciones)

# Definimos como escena inicial al menú
pilas.escenas.EscenaMenu()

pilas.ejecutar()
