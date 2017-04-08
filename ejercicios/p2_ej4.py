#!/usr/bin/env python
from pattern.es import singularize, pluralize

cambiar = {'s':['gato', 'caballo', 'silla'],
        'p':['informaticas', 'psicologicas', 'ingenierias'],
}

def convertir(cambiar):

    print pluralize(cambiar['s'][:])
    

convertir(cambiar)
