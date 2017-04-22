import pilasengine

class ActorPelicula(pilasengine.actores.Actor):

    def iniciar(self, nombre, position):
	self.imagen = pilas.imagenes.cargar('imagenes/'+random.choice(os.listdir('imagenes/')))# if imagen else "imagenes/ribbit7-300px.png"
	self.nombre = nombre
	self.x = position[0][0]
	self.y = position[0][1]
        self.escala=0.3

        self.decir('Hola, me llamo '+ self.nombre)


