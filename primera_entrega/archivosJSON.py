# -*- coding: utf-8 -*-

import json


class GuionParser(object):

    def __init__(self):
        self.guion_parser()

    def archivo_actor(self, actor, dialogo):
        act = actor.replace(' ','')

        filename = "{0}.json".format(act)
        with open(filename, 'w') as outfile:
            json.dump(dialogo, outfile)

    def guion_parser(self):
        guion = open('guion.txt','r')
        lines = guion.readlines()

        secuencia_dialogo = []
        # Genero secuencia y linieas de cada actor
        actor_dialogo = {}
        for dialogo in lines:
            l = dialogo.split(':')
            print(l[1])
            secuencia_dialogo.append(l[0])
            try:
                line = unicode(l[1], encoding='utf-8')
                actor_dialogo[l[0]].append(line)
            except(KeyError):
                actor_dialogo[l[0]] = []
                line = unicode(l[1], encoding='utf-8')
                actor_dialogo[l[0]].append(line)

        for actor, linea in actor_dialogo.iteritems():
            self.archivo_actor(actor, linea)
