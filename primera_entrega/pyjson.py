#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import pprint
import json
def archivo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    d = dialogo.strip()
    data = actor+".json"
    f = open(data, "a")
    json.dump(d, f)
    f.close()

def generar_guion(actor):
#lee el archivo del  actor actor+'txt' y genera una lista con las lineas
    dialogo = []
    archivo_actor = actor+".json"
    with open(archivo_actor, "r") as f:
        d = f.readlines()

    lineas = d[0].split("\"")	
    for linea in lineas:
        dialogo.append(linea)

    for d in dialogo:
	print d
    return dialogo


guion = open("guion.txt","r")

g = guion.readlines()
for l in g:
    linea = l.split(":")
    actor = linea[0].strip()
    dialogo = linea[1]
    archivo_actor(actor, dialogo)


generar_guion("Jorge")



guion.close()


