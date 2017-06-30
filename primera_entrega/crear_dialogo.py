#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pilasengine, random, os,io

class GuionParser(object):


    def __init__(self):
        self.secuencia_dialogo = []
        self.actor_dialogo = {}
        self.guion_parser(self.secuencia_dialogo,self.actor_dialogo)
    def modifica_linea(dialogo):
	p = parse(dialogo)
	lista = p.split(' ') 
        linea = []
        for i in lista:
    	    palabra = i.split('/')
            if palabra[1] == 'VB':
    	        p = conjugate(palabra[0], INFINITIVE)
                linea.append(p)
            elif palabra[1] == 'NN':
    	        linea.append(singularize(palabra[0]))
            else:
    	        linea.append(palabra[0])
        l = " ".join(linea)
        return l

    def guardo_archivo_actor(self,actor,dialogo):
    # Genera NombreActor.txt --> dialogo(lines)
        d = dialogo.strip()
        dm = modifica_linea(d)
        act = actor.replace(' ','')
        filename = "{0}.txt".format(act)
        with open(filename, 'a') as f:
            f.write(d.encode("utf-8") + os.linesep)
        #with io.open(arch, "a", encoding="utf-8") as f:
        #    f.write(d + os.linesep)

    def guion_parser(self,secuencia_dialogo,actor_dialogo):

	guion = io.open('guion.txt', "r", encoding="utf-8")
	lines = guion.readlines()

	# Genero secuencia y linieas de cada actor
	for dialogo in lines:
	    l = dialogo.split(':')
	    secuencia_dialogo.append(l[0])
            self.guardo_archivo_actor(l[0],l[1])
	    
	    try:
		actor_dialogo[l[0]].append(l[1])
	    except(KeyError): 
		actor_dialogo[l[0]] = []
		actor_dialogo[l[0]].append(l[1])


