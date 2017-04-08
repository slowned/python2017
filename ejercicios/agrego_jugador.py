

jugadores = {'mariano':{'nivel':1, 'puntaje_maximo':20, 'tiempo_juego':1},
        'juan':{'nivel':10, 'puntaje_maximo':50, 'tiempo_juego':1},
        'carlo':{'nivel':7, 'puntaje_maximo':40, 'tiempo_juego':1},
        'julio':{'nivel':80, 'puntaje_maximo':10, 'tiempo_juego':1},
        'petizo':{'nivel':75, 'puntaje_maximo':10, 'tiempo_juego':1},
}
#jugadores = {}
corte = True

def agregar_jugador(jugadores):

    nombre = str(raw_input('\ningrese el nrombre del jugador: \t'))
    nivel = raw_input('nivel del jugador: \t')
    puntaje_maximo = raw_input('puntaje maximo: \t')
    tiempo_juego = raw_input('horas jugadas: \t')

    jugador = {'nivel': nivel,
            'puntaje_maximo': puntaje_maximo,
            'tiempo_juego': tiempo_juego
            }

    jugadores[nombre] = jugador

    return jugadores

def listar_jugadores(jugadores):

    for j in jugadores:
        print(j)

def ver_estadistica(name, jugadores):

    print('estadisticas del jugador: ' + name)
    j = jugadores[name]

    for k,v in j.items():
        print k,v

def primeros_10(jugadores):

    list = jugadores.items()

    for i in range(0,len(list[:10])):
        print("\n jugador: " + list[i][0])
        print("puntaje maximo: " + str(list[i][1]['puntaje_maximo']) + "\n")

def ordenados_alfabeticamente(jugadores):
    for j in sorted(jugadores):
        print j
   # list = jugadores.keys()
   # list.sort()
   # for j in list:
   #     print(j)

def ordenados_nivel(jugadores):
    l = []
    list = jugadores.items()

    for i in range(0,len(list)):
        l.append([list[i][1]['nivel'],list[i][0]])
    l.sort(reverse=True)

    print l

while corte:
    print('0 : salir')
    print('1 : agregar jugador')
    print('2 : listar jugadores')
    print('3 : ver estadistica')
    print('4 : primeros 10 puntajes')
    print('5 : listar jugadores ordenados alfabeticamente')
    print('6 : listar jugadores ordenados por nivel')
    o = int(raw_input('ingrese una opcion: \t'))

    if o == 1:
        agregar_jugador(jugadores)
    elif o == 2:
        listar_jugadores(jugadores)
    elif o == 3:
        name = str(raw_input('seleccione un jugador para ver sus estadisticas'))
        ver_estadistica(name,jugadores)
    elif o == 4:
        primeros_10(jugadores)
    elif o == 5:
        ordenados_alfabeticamente(jugadores)
    elif o == 6:
        ordenados_nivel(jugadores)
    elif o == 0:
         corte = False
    else:
        print("ingreso una opcion incorrecta")





