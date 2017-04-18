#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from pattern.es import conjugate, split, parse, INFINITIVE
import json

def guardar_verbos(verbos):
    archivo = open("verbos.txt","w+")
    json.dump(verbos, archivo)   
    archivo.close()
    
def ranking_verbos(parrafo):
    p = parse(parrafo)
    lista = p.split(' ')
    dic = {}
    
    for i in lista:
        palabra = i.split('/')
        vi = conjugate(palabra[0], INFINITIVE)
        if palabra[1] == 'VB':
  	    try:
	        dic[vi] += 1
	    except KeyError:
	        dic[vi] = 1
    return dic
    
parrafo = "Este es un párrafo de prueba. El verbo ser, será el mas utilizado. El otro será crear, por eso se creó la oración de esta manera. Por último, se creará esta oración que posee el tercer verbo: poseer. Nada más que decir."
dic = ranking_verbos(parrafo)
print dic
guardar_verbos(dic)


#ordenar el diccionario key.sort()
#imprimir solo 3