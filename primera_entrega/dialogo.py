import pilasengine

pilas = pilasengine.iniciar()

dialogo = pilas.actores.Dialogo()
mono = pilas.actores.Mono()
otro_mono = pilas.actores.Mono()
dialogo.decir(mono, "Hola, como estas?")
dialogo.decir(otro_mono, "Perfecto!!, gracias...")
dialogo.decir(mono, "genial...")

dialogo.comenzar()

pilas.ejecutar()
