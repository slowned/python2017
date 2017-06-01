import pilasengine
import random
import os

pilas = pilasengine.iniciar()
class ActorPelicula(pilasengine.actores.Actor):


    def iniciar(self, nombre, position, dialogo):
	self.imagen = pilas.imagenes.cargar('imagenes/'+random.choice(os.listdir('imagenes/')))# if imagen else "imagenes/ribbit7-300px.png"
	self.nombre = nombre
	self.lineas=dialogo
	self.x = position[0][0]
	self.y = position[0][1]
        self.escala=0.3

        self.decir('Hola, me llamo '+ self.nombre)

    def get_nombre(self):
	return str(self.nombre)

    def get_linea(self):
	l=self.lineas[0]
	self.lineas.remove(l)
	return l

