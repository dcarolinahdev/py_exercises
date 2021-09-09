# -*- coding: utf-8 -*-

def more_exercises():
    palabra = 'cARolIna   '
    print("-------------------------")
    print('\nMore functions [word: '+palabra+']')
    print("Total Length: " + str(len(palabra)) + ".")

    palabra = palabra.strip()
    print("Strip mode: " + palabra + ".")
    print("Strip length: " + str(len(palabra)))

    print("Capitalize: " + palabra.capitalize())
    print("Upper mode: " + palabra.upper())
    palabra = palabra.lower()
    print("Lower mode: " + palabra)

    print("\nFirst 3 char [0:3]: " + palabra[0:3])
    print("First 3 char [:3]: " + palabra[:3])
    print("Last 3 char [5:]: " + palabra[5:])
    print("Last 3 char [-3:]: " + palabra[-3:])
    print("palabra[:-3]: " + palabra[:-3])
    print("palabra[::2]: " + palabra[::2])
    print("palabra[::-1]: " + palabra[::-1])


def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
    more_exercises()


if __name__ == '__main__':
    run()
