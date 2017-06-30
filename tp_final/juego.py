# -*- encoding: utf-8 -*-
import pilasengine

import CuentosPersonalizado, escena_opciones, escena_menu, escena_seleccion

pilas = pilasengine.iniciar()


# Vinculamos las escenas

pilas.escenas.vincular(escena_seleccion.Seleccion)
pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_opciones.Opcion)
pilas.escenas.vincular(CuentosPersonalizado.CuentosPersonalizado)

# Definimos como escena inicial al menú
pilas.escenas.EscenaMenu()

pilas.ejecutar()
