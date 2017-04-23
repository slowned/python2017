import pilasengine
import random
import os

pilas = pilasengine.iniciar()
dialogo=pilas.actores.Dialogo()
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

    def get_lineas(self):
	return self.lineas

    def eliminar_linea(self, valor):
	self.lineas.remove(valor)

#def dialogar():
#    dialogo.comenzar()
#actores= {}
#pos1=[(50,50)]
#pos2=[(5,-47)]
#linea1=['lineas de juan']
#linea2=['lineas de carlo 11','lineas de carlo 22 ']
#juan = ActorPelicula(pilas,nombre='juan carlos',position=pos1,dialogo=linea1)
#carlo = ActorPelicula(pilas,nombre='carlo',position=pos2,dialogo=linea2)
#
##actores[carlo.get_nombre()]=carlo.get_lineas()
##actores[juan.get_nombre()]=juan.get_lineas()
#
#
#actores[carlo.get_nombre()]=carlo
#actores[juan.get_nombre()]=juan
#
#for k,v in actores.items():
##    print (k,v.get_lineas()[0])
#    dialogo.decir(actores[k],v.get_lineas()[0])
##    v.eliminar_linea(v.get_lineas()[0])
##print(carlo.get_lineas())
#
##dialogo.comenzar()
#
#boton=pilas.actores.Boton()
#boton.x=60
#boton.y=-60
#boton.conectar_presionado(dialogar)
##boton.conectar(dialogar(dialogo))
#pilas.ejecutar()
