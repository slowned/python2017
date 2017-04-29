# -*- coding: utf-8 -*-

import json


class GuionParser(object):
  
  
    def __init__(self):
        self.actor_dialogo = {}
        self.secuencia_dialogo = []
        self.guion_parser(self.actor_dialogo,self.secuencia_dialogo)

    def archivo_actor(self, actor, dialogo):
        act = actor.replace(' ','')

        filename = "{0}.json".format(act)
        with open(filename, 'w') as outfile:
            json.dump(dialogo, outfile)

    def guion_parser(self,actor_dialogo,secuencia_dialogo):
        guion = open('guion.txt','r')
        lines = guion.readlines()

        # Genero secuencia y linieas de cada actor
        for dialogo in lines:
            l = dialogo.split(':')
            secuencia_dialogo.append(l[0])
            try:
                line = unicode(l[1], encoding='utf-8')
                actor_dialogo[l[0]].append(line)
            except(KeyError):
                actor_dialogo[l[0]] = []
                line = unicode(l[1], encoding='utf-8')
                actor_dialogo[l[0]].append(line)

