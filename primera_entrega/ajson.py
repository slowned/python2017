#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import json
guion = open('guion.txt','r')
def guardo_dialogo_actor(actor,dialogo):
# Genera NombreActor.txt --> dialogo(lines)
    arch = actor+'JSON.txt'
    with open(arch, 'a') as f:
	json.dump(dialogo,f)
    f.close()

for linea in guion:
    d = linea.split(':')
    actor = d[0]
    l = d[1] 
    guardo_dialogo_actor(actor,str(l))

a = open('SusanaJSON.txt','r')
data = json.load(a)
print(json.dump(data))
a.close()

