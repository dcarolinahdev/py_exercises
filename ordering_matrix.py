# -*- coding: utf-8 -*-
import numpy as np
from random import randint

print ("Para empezar le solicitaré el tamaño de la matriz (f y c) y el rango en el cual se generarán los valores aleatorios (0 a k)")
print ()

f = int(input("Dígame el número de filas de la matriz: "))

c = int(input("Dígame el número de columnas de la matriz: "))

k = int(input("Dígame el valor máximo an generar en la matriz: "))

print ()
print ("La siguiente matriz ha sido creada: ")
initial_matrix = []
for i in range (f):
	aux_list = []
	for j in range (c):
		aux_list.append(randint(0, k))
	initial_matrix.append(aux_list)
print (initial_matrix)

counting_list = np.zeros(k+1)
print ()
print ("Conteo de valores: ")
for x in initial_matrix:
	for y in range(k+1):
		counting_list[y] += x.count(y)
print (counting_list)

orden = input("¿Cómo desea ordenar la matriz ascendente (A) o descendente (B)?")
while (not ((orden == 'A') or (orden == 'B'))):
	orden = input("¿Cómo desea ordenar la matriz ascendente (A) o descendente (B)?")
if orden == 'A':
	start_count = int(counting_list[0])
	start_value = 0
	seq = 1
else:
	start_count = int(counting_list[-1])
	start_value = k
	seq = -1

print ()
print ("Esta es su matriz ordenada: ")
ordered_matrix = []
for i in range (f):
	aux_list = []
	for j in range (c):

		while (len(aux_list) < k):
			if (len(aux_list)+start_count) < k:
				for n in range(start_count):
					aux_list.append(start_value)
				start_value = start_value + seq
				start_count = int(counting_list[start_value])
			else:
				aux_k = k-len(aux_list)
				for m in range(aux_k):
					aux_list.append(start_value)
				start_count = int(counting_list[start_value]) - aux_k
		
	print (aux_list)
	# ordered_matrix.append(aux_list)
# print (ordered_matrix)
