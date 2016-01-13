#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script para modificar la temperatura de la cama caliente en un gcode
# Autor: Santiago López Pina
# Fecha: 28 de Octubre de 2015

# Paquetes para parsear los argumentos en la llamada
import argparse


# Variable con los argumentos
ap = argparse.ArgumentParser()
# Argumento con el nombre del fichero gcode a editar
ap.add_argument("-g", "--gcode", required=True,
                help="path to the Gcode configuration file")
# Argumento con el setpoint de temperatura de la cama caliente
ap.add_argument("-t", "--temp", required=True,
                help="Temp to the set the bed")
# Diccionario con los argumentos anteriores
args = vars(ap.parse_args())
# Variable con el nombre del fichero a editar
f_gcode = args["gcode"]
# Variable con el nombre del fichero destino
f_gcode2 = str(args["temp"]) + str(args["gcode"])
# Comando a reemplazar
command = "M109 S{0} ;Uncomment to add your own temperature line".format(args[
                                                                         "temp"])


# Abrimos el fichero origen como lectura
f1 = open(f_gcode, 'r')
# Abrimos el fichero destino como escritura
f2 = open(f_gcode2, 'w')
# Por cada linea en el fichero de origen
for line in f1:
    # Escribimos en el fichero de destino y reemplazamos la linea con el
    # comando de la cama caliente
    f2.write(line.replace(
        ';M190 S70 ;Uncomment to add your own bed temperature line', command))
# Cerramos ambos ficheros
f1.close()
f2.close()
