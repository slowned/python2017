# -*- coding: utf-8 -*-

import io, os

class HistoryParser(object):

    def __init__(self):
        self.scenes_parser()

    def save_scene(self,scene,line):
        # Genera Escena.txt  
        print (scene)
        filename = "{0}.txt".format(scene)
        with open(filename, 'a') as f:
            f.write(line.encode("utf-8") + os.linesep)

    def new_scene(self,line):
        # Rotorna el nombre de la escena [Escena1,escena1.txt] >> "Escena1"
        l = str(line.strip('[').strip(']').replace(' ','').split(','))
        return l[0]

    def scenes_parser(self):
        history = io.open('historia.txt', "r", encoding="utf-8")
        lines = history.readlines()
        history.close()

        for line in lines:
            if (line[0] == '['):
                scene = self.new_scene(line)
            self.save_scene(scene,line)


