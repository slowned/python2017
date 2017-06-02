import pilasengine
import random
import os

pilas = pilasengine.iniciar()
class ActorPelicula(pilasengine.actores.Actor):


    def iniciar(self, nombre, dialogo):
	self.imagen = pilas.imagenes.cargar('imagenes/'+random.choice(os.listdir('imagenes/')))# if imagen else "imagenes/ribbit7-300px.png"
	self.nombre = nombre
	self.lineas = dialogo
	self.x = random.randrange(-100,100)
	self.y = random.randrange(-100,100) 
        self.escala=0.3

    def get_nombre(self):
	return str(self.nombre)

    def get_linea(self):
	l=self.lineas[0]
	self.lineas.remove(l)
	return l

