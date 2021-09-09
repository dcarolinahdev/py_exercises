# -*- coding: utf-8 -*-

def run():
    num_potencias = int(input('¿Cuantas potencias de 2?: '))
    indice = 0
    while(indice < num_potencias):
        print("2 elevado a "+str(indice)+" es: "+str(pow(2,indice)))
        indice += 1


if __name__ == '__main__':
    run()