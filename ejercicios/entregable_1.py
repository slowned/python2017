#!/usr/bin/env python


frase = str(raw_input('ingrese una frase: \n')).lower()
palabra = str(raw_input('ingrese un string: \n')).lower()

lista_frase = frase.split(' ')

cant = 0

for p in lista_frase:
    if (p.count(palabra) > 0):
        cant += 1

print('el string ' +  palabra + ' ' + 'aparece' + ' ' + str(cant) + ' ' + 'veces en la frase')

