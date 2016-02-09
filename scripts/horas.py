from math import floor


def minutestohours(minutes):
    print("{} horas y {} minutos".format(floor(minutes/60), minutes % 60))


def main():
    minutos = int(input("inserte minutos"))
    minutestohours(minutos)

main()
