import pilasengine
import .crear_actor

pilas = pilasengine.iniciar()

dialogo = pilas.actores.Dialogo()
mono = pilas.actores.Mono()
otro_mono = pilas.actores.Mono()
dialogo.decir(mono, "Hola, como estas?")
dialogo.decir(otro_mono, "Perfecto!!, gracias...")
dialogo.decir(mono, "genial...")

dialogo.comenzar()

char = ActorPelicula(pilas, nombre='kian', position([(2,4)])
pilas.ejecutar()
