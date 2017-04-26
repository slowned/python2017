#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import json

def archivo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    d = dialogo.strip()
    act = actor.replace(' ','')
    data = act+".json"
    f = open(data, "a")
    json.dump(d, f)
    f.close()

def generar_guion(actor):
#lee el archivo del  actor actor+'txt' y genera una lista con las lineas
    dialogo = []
    act = actor.replace(' ','')
    archivo_actor = act+".json"
    with open(archivo_actor, "r") as f:
        d = str(f.readlines())
    for line in d:
	dialogo.append(line)
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


