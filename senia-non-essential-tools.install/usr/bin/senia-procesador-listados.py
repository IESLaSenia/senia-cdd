#!/usr/bin/python3

# SCRIPT para la creacion de directorios con nombres de alumnos para
# Itaca

# Version 0.1

import xlrd
import sys
import os
import unicodedata
import time



if len(sys.argv) < 3:
	print(" [ERROR] : Al menos dos argumentos")
	
	sys.exit(1)

# Directorio donde generaremos la estructura
diraux=sys.argv[1]

fichero=sys.argv[2]
if not os.path.isfile(fichero):
	print(" [ERROR] : El fichero : "+fichero+ " No existe" )
	sys.exit(1)

# Utilidades varias
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))


# Tenemos algunas cosillas ya...
# Veamos
book = xlrd.open_workbook(fichero)
sh = book.sheet_by_index(0)
for rx in range(sh.nrows):
	
	aux_n = sh.cell(rx,1).value.replace(" ","-")
	nombre=elimina_tildes(aux_n)
	aux_a = sh.cell(rx,2).value.replace(" ","-")
	apellido=elimina_tildes(aux_a)
	
	ruta=diraux+"/"+os.path.basename(fichero).split(".")[0]+"/"+apellido+"_"+nombre
	if apellido != "Apellido1":
		print(" [ Creando ] : "+ruta)
		if not os.path.isdir(ruta):
			os.makedirs(diraux+"/"+os.path.basename(fichero).split(".")[0]+"/"+aux_a+"_"+aux_n)
			pass
	
	
	
	
	



