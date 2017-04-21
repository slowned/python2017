
import pilasengine, os, random

pilas = pilasengine.iniciar()

class ActorPelicula(pilasengine.actores.Actor):

    def iniciar(self,image, name):
	self.imagen = 'imagenes/'+image
	self.nombre = name

pilas.actores.vincular(ActorPelicula) #VINCULAMOS EL ACTOR PERSONALIZADO

image = str(random.choice(os.listdir('imagenes/'))
list_name = ['Juan','Pedro','Antonia','Pilar']
name = random.choice(lista_nombres)

character = pilas.actores.ActorPelicula(image,name)

pilas.ejecutar()
