#!/usr/bin/env python
# Script para python que abre todos los gcodes en el mismo directorio en el que
# se encuentre el script y calcula el tiempo estimado por cura.
# Es necesario geenrar el gcode con cura y que en el start gcode:
# ;Sliced at: {day} {date} {time}
# ;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
# ;Print time: {print_time}
# ;Filament used: {filament_amount}m {filament_weight}g
# ;Filament cost: {filament_cost}
# ;M190 S{print_bed_temperature} ;Uncomment to add your own bed temperature line
# ;M109 S{print_temperature} ;Uncomment to add your own temperature line

from math import floor
import os

__author__ = "SLP"


class estimate():

    def __init__(self):
        self.__gcodes = []
        self.__time = [0, 0]

    def searchgcodes(self):
        directory = os.listdir()
        self.__gcodes = [files for files in directory if files.endswith(
                    ".gcode")]

    def minutestohours(self):
        self.__time[0] = self.__time[0] + floor(self.__time[1]/60)
        self.__time[1] = self.__time[1] % 60

    def estimatetime(self):
        for gcode in self.__gcodes:
            with open(gcode, 'r') as infile:
                lines = infile.readlines()

            dic = (str(lines[3])[13:-1].replace('hours', '').replace(
                    ' minutes', '').split('  '))

            if len(dic) == 1:
                dic.append(dic[0])
                dic[0] = 0

            for i in range(2):
                self.__time[i] = self.__time[i] + int(dic[i])

    def gettime(self):
        return self.__time


def main():
    s = estimate()
    s.searchgcodes()
    s.estimatetime()
    s.minutestohours()
    tiempo = s.gettime()
    print("Duración estimada: {} horas y {} minutos".format(tiempo[0],
          tiempo[1]))

if __name__ == '__main__':
    main()
