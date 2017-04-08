
jugadores = {}
corte = True
opciones = {0: agregar_jugador, 1: listar_jugador, 2: ver_estadistica_jugador}

def agregar_jugador():
    nombre = str(raw_input('\ningrese el nrombre del jugador: \t'))
    nivel = raw_input('nivel del jugador: \t')
    puntaje_maximo = raw_input('puntaje maximo: \t')
    tiempo_juego = raw_input('horas jugadas: \t')

    jugador = {'nivel': nivel,
            'puntaje_maximo': puntaje_maximo,
            'tiempo_juego': tiempo_juego
            }
    jugadores[nombre] = jugador

def listar_jugador(jugadores):
    for j in jugadores:
        print(j.key())

def ver_estadistica_ugado(jugadores):
    name = str(raw_input('seleccione un jugador para ver sus estadisticas')

#while True:
#    print('1 : agregar jugador')
#    print('2: listar jugadores')
#    print('3 : ver estadistica')
#    option = int(raw_input('ingrese una opcion'))
#    opciones[option]
