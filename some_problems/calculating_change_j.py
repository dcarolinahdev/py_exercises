import sys
import math

valorMonedas = [1000, 500, 200, 100, 50]

def calcularCambio(total, pago):
	print('\nPagando '+str(total)+' con '+str(pago))
	my_answer = []

	subtraction = pago - total
	for moneda in valorMonedas:
		print('\n- Evaluando '+str(subtraction)+' para '+str(moneda))
		aux = subtraction / moneda
		print('moneda '+str(moneda)+' se encuentra '+str(aux)+' veces')
		ciclo = int(math.floor(aux))
		for i in range(ciclo):
			my_answer.append(moneda)
		subtraction = subtraction - (moneda * math.floor(aux))
		print('ahora resta '+str(subtraction))

	print('\nSolución: '+str(my_answer))

total = int(sys.argv[1])
pago = int(sys.argv[2])

calcularCambio(total, pago)
