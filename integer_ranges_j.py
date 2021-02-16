# -*- coding: utf-8 -*-

def version_uno():
	for x in range (1,15):
		if x>0 and x < 5:
			print("El número %s se encuentra entre [1-5]" % x)
		elif x>5 and x <= 10:
			print("El número %s se encuentra entre [6-10]" % x)
		elif x>=11 and x < 16:
			print("El número %s se encuentra entre [11-16]" % x)

def version_dos():
	split_num = 5
	for x in range (1,16):
		if x>0 and x <= 5:
			print("El número %s se encuentra entre [1-5]" % x)
		elif x>5 and x <= 10:
			print("El número %s se encuentra entre [6-10]" % x)
		elif x>10 and x <= 16:
			print("El número %s se encuentra entre [11-15]" % x)
	return None

print ("Pregunta 2. Escriba un número entre 1 y 16, la función original está comentada, se ejecuta la función corregida")
print ("Respuesta: ")
version_dos()
