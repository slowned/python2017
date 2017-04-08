#!/usr/bin/env python

jugadores = {'mariano':{'nivel':1, 'puntaje_maximo':20, 'tiempo_juego':1},
        'juan':{'nivel':10, 'puntaje_maximo':50, 'tiempo_juego':1},
        'carlo':{'nivel':7, 'puntaje_maximo':40, 'tiempo_juego':1},
        'julio':{'nivel':80, 'puntaje_maximo':10, 'tiempo_juego':1},
        'petizo':{'nivel':75, 'puntaje_maximo':10, 'tiempo_juego':1},
}

list = jugadores.items()

l = jugadores.keys()

a = []

for i in range(0,len(list)):
    a.append([list[i][1]['nivel'],list[i][0]])
a.sort(reverse=True)
print a
##alfabeticamente
#l.sort()
#for j in l:
#    print(j)
##10 primeros puntajes
#for i in range(0,len(list[:10])):
#    print("jugador: " + list[i][0])
#    print("puntaje maximo: " + str(list[i][1]['puntaje_maximo']) + "\n")
#





