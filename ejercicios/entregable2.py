#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from pattern.es import conjugate, split, parse, INFINITIVE
from collections import Counter
import json

def guardar_verbos(verbos):
    archivo = open("verbos.txt","w+")
    json.dump(verbos, archivo)   
    archivo.close()
    
def ranking_verbos(parrafo):
    p = parse(parrafo)
    lista = p.split(' ')
    dic = {}
    cnt = Counter()
    
    for i in lista:
        palabra = i.split('/')
        vi = conjugate(palabra[0], INFINITIVE)
        if palabra[1] == 'VB':
	    cnt[vi] += 1

    mas_usados = cnt.most_common(3)
    for i in range(0,3):
        dic[mas_usados[i][0]] = mas_usados[i][1]

    return dic 
    
parrafo = "Este es un párrafo de prueba. El verbo ser, será el mas utilizado. El otro será crear, por eso se creó la oración de esta manera. Por último, se creará esta oración que posee el tercer verbo: poseer. Nada más que decir."
dic = ranking_verbos(parrafo)
print dic
guardar_verbos(dic)


