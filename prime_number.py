# -*- coding: utf-8 -*-

def es_primo(num):
	for n in range(2, num):
		if num % n == 0:
			print("No es primo", n, "es divisor")
			return False
	print("Es primo")
	return True

def run():
    number = int(input('Escribe el número que deseas saber si es primo o no: '))
    es_primo(number)

if __name__ == '__main__':
    run()