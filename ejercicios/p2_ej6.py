#!/usr/bin/env python
from os import listdir
import os

path = '/home/moll/Desktop/python2017'
files = listdir(path)

for f in files:
    a = os.stat(f)
    print('nombre: ' + f + ' tamanio: ' + str(a.st_size) + ' fecha ultimo acceso: '+ str(a.st_atime))
