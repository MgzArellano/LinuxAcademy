#!/bin/python

import os

xfile = open('jsonFull.json','r+')
xfile = open('jsonFull.json', 'a')  # con esta opción a de append, agregamod líneas con la instrucción
                                    # xfile.writelines(['linea1\n', 'linea2\n'])


## otra forma de agregar líneas
# with open('jsonFull.json') as xfile:
    #xfile.write("linea\n")

xfile.seek(-1, os.SEEK_END)

#for line in xmen_file:
#    contador = contador+1
#    print(str(contador) +"- "+line)

xfile.write("New line 1")
xfile.write("New line 2")
xfile.write("New line 3")


#print(xfile.read())
xfile.close()

