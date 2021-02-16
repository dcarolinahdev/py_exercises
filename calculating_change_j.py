import sys
import math

valorMonedas = [500, 200, 100, 50]

def calcularCambio(total, pago):
	my_answer = []

	subtraction = pago - total

	for moneda in valorMonedas:
		aux = subtraction / moneda
		# print(aux)
		for i in range(int(math.floor(aux))):
			my_answer.append(moneda)
		subtraction = subtraction - (moneda * math.floor(aux))
		# print(subtraction)
		if subtraction < moneda:
			break

	print(my_answer)

total = int(sys.argv[1])
pago = int(sys.argv[2])

calcularCambio(total, pago)
