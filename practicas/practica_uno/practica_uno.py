
def ejercicio_cinco():
    frase = "Si trabajás mucho CON computadoras, eventualmente encontrarás \
    que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear \
    realizar una búsqueda y reemplazo en un gran número DE archivos de texto, \
    o renombrar y reorganizar un montón de archivos con fotos de una manera \
    compleja. Tal vez quieras escribir alguna pequeña base de datos \
    personalizada, o una aplicación especializada con interfaz gráfica, o \
    UN juego simple."

    sin_repetir = []
    lista_frase = frase.lower().split(' ')

    for palabra in lista_frase:
        if frase.count(palabra) <= 1:
            sin_repetir.append(palabra)

    print(sin_repetir)


def ejercicio_seis():
    historial = {} # { nombre_jugador: {'nombre': "juan", 'nivel': 7, 'puntaje': 939, 'timepo': 1.30} }

    nombre = input('Nombre del jugador: ').lower()
    nivel = input('Nivel: ')
    puntaje = input('Puntaje: ')
    tiempo = input('Tiempo de juego: ')

    historial[nombre] = {
        'nivel': nivel,
        'puntaje': puntaje,
        'tiempo': tiempo,
    }
